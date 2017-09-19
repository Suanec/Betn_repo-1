#!/usr/bin/env python


# parse arguments
import argparse
import json

parser = argparse.ArgumentParser(description='Integrate Scikit-learn.')
parser.add_argument('--train-data', type=str)
parser.add_argument('--estimator', type=str)
parser.add_argument('--init-args', type=json.loads, default={})
parser.add_argument('--model-dir', type=str, default=None)

args = parser.parse_args()
print(args)

# load data
from sklearn.datasets import load_svmlight_file
## TODO: 详细参数
X, y = load_svmlight_file(args.train_data)

# init estimator
import pydoc
import sklearn

version = '.'.join(sklearn.__version__.split('.')[0:2])

if version == '0.18':
    class_register = {
            'lr': 'sklearn.linear_model.LogisticRegression'
            }
else:
    class_register = {}
    print("WARN: sklearn version {} is not tested by now".format(version))

cls_name = class_register.get(args.estimator, args.estimator)
cls = pydoc.locate(cls_name)
obj = cls(**args.init_args)

# fit
obj.fit(X, y)
print(obj)

# save
from sklearn.externals import joblib

if args.model_dir:
    joblib.dump(obj, args.model_dir)

# load
## obj = joblib.load(args.model_dir)
