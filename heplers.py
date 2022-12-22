import datetime

def formatDate(tf:datetime)->str:
    return str(tf.year) +'-'+str(tf.month)+'-'+str(tf.day)

def formatDateTime(tf:datetime)->str:
    return formatDate(tf)+' ' + tf.time.hour+':'+tf.time.minute+' '+tf.time.second