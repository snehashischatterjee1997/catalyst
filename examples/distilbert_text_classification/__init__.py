# flake8: noqa
# pylint: disable=unused-import

from catalyst.contrib.models.nlp import BertClassifier
from catalyst.dl import registry, SupervisedRunner as Runner

from .experiment import Experiment

registry.Model(BertClassifier)
