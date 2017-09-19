sh -x pull-sample.sh -n dlmodel.sample -p ./
sh -x training-model.sh
sh -x push-model.sh -n dlmodel.model -p ./dlmodel.model
