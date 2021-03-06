'''
Copyright 2014-2017 EMBL - European Bioinformatics Institute, Wellcome
Trust Sanger Institute, GlaxoSmithKline and Biogen

This software was developed as part of Open Targets. For more information please see:

	http://targetvalidation.org

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import re
import sys
import iso8601
import types
import json
import logging

__author__ = "Gautier Koscielny"
__copyright__ = "Copyright 2014-2017, Open Targets"
__credits__ = ["Gautier Koscielny", "Samiul Hasan"]
__license__ = "Apache 2.0"
__version__ = "1.2.5"
__maintainer__ = "Gautier Koscielny"
__email__ = "gautierk@targetvalidation.org"
__status__ = "Production"

logger = logging.getLogger(__name__)

"""
https://raw.githubusercontent.com/opentargets/json_schema/master/src/evidence/linkout/linkout.json
"""
class Linkout(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param url = None
  :param nice_name = None
  """
  def __init__(self, url = None, nice_name = None):
    
    """
    Name: url
    Type: string
    Required: {True}
    String format: uri
    """
    self.url = url
    
    """
    Name: nice_name
    Type: string
    Required: {True}
    """
    self.nice_name = nice_name
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.url:
        obj.url = clone.url
    if clone.nice_name:
        obj.nice_name = clone.nice_name
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['url','nice_name']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.warn("Linkout - DictType expected - {0} found\n".format(type(map)))
      return
    if  'url' in map:
        obj.url = map['url']
    if  'nice_name' in map:
        obj.nice_name = map['nice_name']
    return obj
  
  def validate(self, logger, path = "root"):
    """
    Validate class Linkout
    :returns: number of errors found during validation
    """
    error = 0
    # url is mandatory
    if self.url is None :
        logger.error("Linkout - {0}.url is required".format(path))
        error = error + 1
    if self.url and not isinstance(self.url, basestring):
        logger.error("Linkout - {0}.url type should be a string".format(path))
        error = error + 1
    # nice_name is mandatory
    if self.nice_name is None :
        logger.error("Linkout - {0}.nice_name is required".format(path))
        error = error + 1
    if self.nice_name and not isinstance(self.nice_name, basestring):
        logger.error("Linkout - {0}.nice_name type should be a string".format(path))
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.url is None: classDict['url'] = self.url
    if not self.nice_name is None: classDict['nice_name'] = self.nice_name
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
