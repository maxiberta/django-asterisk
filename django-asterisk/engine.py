# coding=utf-8

import asterisk.manager
import threading
import datetime
import settings
from models import Call

def handle_shutdown(event, manager):
   manager.close()
   # we could analize the event and reconnect here

def handle_event(event, manager, call):
   if event.name == 'Hangup':
      call.disposition = event.get_header('Cause-txt')
      call.cause = event.get_header('Cause')
      call.duration = (datetime.datetime.now() - call.start).seconds
      call.save()
      with manager.lock:
          manager.lock.notifyAll()

def make_call(call):
  manager = asterisk.manager.Manager()
  manager.lock = threading.Condition()
  try:  
    try:
	call.start = datetime.datetime.now()

        # connect to the manager
        manager.connect(settings.AST_HOST)
        manager.login(settings.AST_USER, settings.AST_PASS)

        # register some callbacks
        manager.register_event('Shutdown', handle_shutdown) # shutdown
        manager.register_event('*', lambda event, manager: handle_event(event,manager,call)) # catch all

        # get a status report
        response = manager.originate(call.channel, call.extension, call.context, settings.AST_PRIO, settings.AST_TIMEOUT_ORIGINATE * 1000, call.caller_id)
        call.response = response.get_header('Response')
        with manager.lock:
            manager.lock.wait(settings.AST_TIMEOUT_HANGUP)

    except asterisk.manager.ManagerSocketException, (errno, reason):
       msg = "Error connecting to the manager: %s" % reason
       call.disposition = msg
       raise
    except asterisk.manager.ManagerAuthException, reason:
       msg = "Error logging in to the manager: %s" % reason
       call.disposition = msg
       raise
    except asterisk.manager.ManagerException, reason:
       msg = "Error: %s" % reason
       call.disposition = msg
       raise

  finally:
    # remember to clean up
    call.save()
    manager.close()
 
def call_all(calls):
    import logging
    import time
    start_time = time.time()
    answered = 0
    not_answered = 0
    errors = 0
    
    for call in calls:
        try:
             logging.info('calling "%s" (%s) on context "%s"' % (call.related_object, call.channel, call.context))
             make_call(call)
             if call.cause in ('4', '16'):
                 answered += 1
             else:
                 not_answered += 1
        except:
             errors += 1

    logging.info("Call stats: %s answered; %s not answered; %s error done in %.2f seconds" % (answered, not_answered, errors, time.time() - start_time))
    return answered, not_answered, errors

