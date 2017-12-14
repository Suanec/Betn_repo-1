# WORK_SPACE ALIASES
CDD="cd /Users/enzhao/suanec//ksp/dataflow"
CDO="cd /Users/enzhao/suanec/ksp/dockerTest"
CDL="cd /Users/enzhao/suanec/ksp/dlontf"
CFD="cd /Users/enzhao/suanec/weibo/betn_repo/dataflow/GBDT+LR/dataflow/framework"
CKD="cd /Users/enzhao/suanec/ksp/dispatch/controlCenter/weiclient/release/weiclient-run"
CGD="cd /Users/enzhao/suanec/ksp/dispatch/controlCenter/weiclient/weiclient/main/"
D="cp /Users/enzhao/suanec/ksp/dataflow/framework/target/data-flow-2.0.0-SNAPSHOT-shade.jar ./"
UP="sh -x /Users/enzhao/suanec/libs/envs/upload_dataflow_jar.sh"
CC="cp -rv /Users/enzhao/suanec/ksp/dispatch/controlCenter/weiclient/weiclient/libs/* ./libs/"
K8S="sh $ENV_HOME/k8s-kubectl.sh"
ENV_HOME="/Users/enzhao/suanec/libs/envs"
TOY="sh $ENV_HOME/tfoy.sh"
alias showckd='echo -e " CDD:$CDD \n CDO:$CDO \n CFD:$CFD \n CKD:$CKD \n D:$D \n UP:$UP"'
alias showckd='cat ${ENV_HOME}/ckd.sh | grep -v "alias" | grep -v "#" | uniq'
alias cdd=$CDD
alias cdo=$CDO
alias cdl=$CDL
alias cfd=$CFD
alias ckd=$CKD
alias cgd=$CGD
alias d=$D
alias up=$UP
alias cc=$CC
alias k8s=$K8S
alias upwc="cp -r /Users/enzhao/suanec/ksp/dispatch/git-weiclient/weiclient/py-weiclient/src/libs /Users/enzhao/suanec/ksp/dispatch/weiclient-run" 
alias up="cp -r /Users/enzhao/suanec/ksp/dispatch/git-weiclient/weiclient/py-weiclient/src/libs /Users/enzhao/suanec/ksp/dispatch/weiclient-run/"
alias toy="$TOY"
alias waiccc="sh $ENV_HOME/query_jobKey.sh"
alias rsyncshow="echo 'rsync -vz 10.77.29.68::backup/weiflow/'"

#REVIEW_LIST
GEN_REVIEW_LIST_FILE="/Users/enzhao/suanec/weibo/betn_repo/joyCodes/genReviewListDate.scala"
alias reviewlist="scala ${GEN_REVIEW_LIST_FILE}"

# ALIAS
alias suanec="sh $ENV_HOME/suanec@175.sh"
alias root175="sh $ENV_HOME/Zroot@175.sh"
alias suanecr="sh $ENV_HOME/Zroot@21640.sh"
alias hadoop175="sh $ENV_HOME/hadoop@175.sh"
alias root176="sh $ENV_HOME/Zroot@176.sh"
alias hadoop176="sh $ENV_HOME/hadoop@176.sh"
alias suanecg="sh $ENV_HOME/g-channel.sh"
alias liaobog="sh $ENV_HOME/liaobo.sh"
alias showg="sh $ENV_HOME/show-channel.sh"
alias suaneclt="sh $ENV_HOME/LT1-channel.sh"
alias suaneclt2="sh $ENV_HOME/LT2-channel.sh"
alias suanecdx="sh $ENV_HOME/DX1-channel.sh"
alias suanecdx2="sh $ENV_HOME/DX2-channel.sh"
alias wser="sh $ENV_HOME/start_HTTPServer.sh"
alias ip="sh $ENV_HOME/getIP.sh"
alias c="clear"
alias datemd="scala /Users/enzhao/suanec/weibo/betn_repo/joyCodes/genReviewListDate.scala $*"

# Linux Alias
alias ll="ls -ltah"
alias lsz='ls -lSah'
alias wsp="cd ~/suanec/ksp"
alias ecp="cp -rvfp"
alias ldir='ls -lh|grep ^d'
alias h5='head -5'
alias h1='head -1'
alias jj="jobs -l"
alias tf="tail -f"
alias lduh="du -d 1 -h"
alias dush="du -sh ."
alias rmr="rm -rvf"

# hdfs Alias
alias fsls="hadoop fs -ls "
alias fsmv="hadoop fs -mv "
alias fsrmr="hadoop fs -rm -r "
alias fscat="hadoop fs -cat "
alias fstail="hadoop fs -tail "
alias fs="hadoop fs"

# git ALIASES
alias ga="git add"
alias gs="git status"
alias gc="git commit"
alias gp="git push"
alias gpp="git pull"
alias gclone="git clone"
alias ginit="git init"
alias gadd="git add"
alias gmv="git mv"
alias greset="git reset"
alias grm="git rm"
alias gbisect="git bisect"
alias ggrep="git grep"
alias glog="git log"
alias gshow="git show"
alias gstatus="git status"
alias gbranch="git branch"
alias gcheckout="git checkout"
alias gcommit="git commit"
alias gdiff="git diff"
alias gmerge="git merge"
alias grebase="git rebase"
alias gtag="git tag"
alias gfetch="git fetch"
alias gpull="git pull"
alias gpush="git push"

