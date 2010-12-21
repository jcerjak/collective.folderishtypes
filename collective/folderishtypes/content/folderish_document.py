# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import document
from Products.ATContentTypes.content import folder

from collective.folderishtypes.interfaces import IFolderishDocument
from collective.folderishtypes.config import PROJECTNAME

folder_schema = folder.ATFolderSchema.copy()
document_schema = document.ATDocumentSchema.copy()

class FolderishDocument(folder.ATFolder, document.ATDocument):
    implements(IFolderishDocument)

    portal_type = 'Folderish Document'
    _at_rename_after_creation = True
    schema = folder_schema.update(document_schema)

atapi.registerType(FolderishDocument, PROJECTNAME)
