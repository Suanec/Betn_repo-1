#!/bin/bash

SELF_DIR="$( cd "$( dirname "$0" )" && pwd )"
grep "URL:" weiflow-from-weiclient.log | uniq | awk -F": http:" '{print $2}' | awk -F"\/" '{print $5}' | xargs yarn application -kill
