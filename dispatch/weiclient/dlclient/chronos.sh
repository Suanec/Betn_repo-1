#!/bin/sh
#发送请求
curl http://10.77.31.203:4400/kairos?job=%7b%22owner%22%3a%22lihan3%22%2c%22name%22%3a%22lihan_test%22%2c%22command%22%3a%22cd+%2fdata0%2fusers%2fjihui2%2fctr%3b+python+t.py++--distributed+False%22%2c%22user%22%3a%22root%22%2c%22deleNotCrontJob%22%3atrue%2c%22host%22%3a%2210.77.9.131%22%7d
#http://10.77.31.203:4400/kairos?job=
#{"owner":"lihan3","name":"lihan_test",
#"command":"cd /data0/users/jihui2/ctr; 
#python t.py  —distributed False 1> t.py.out 2>&1",
#"user":"root","deleNotCrontJob":true,"host":"10.77.9.131"}


