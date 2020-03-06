import os

StorageAccountKey = os.environ.get('STORAGE_ACCOUNT_KEY')

azure_storage_connectors = {
    'connection_string': 'DefaultEndpointsProtocol=https;AccountName=funcstoragetest;AccountKey={};EndpointSuffix=core.windows.net'.format(
        StorageAccountKey),
    'storage_account_name': 'funcstoragetest',
    'inbox_container': '01inbox',
    'unknown_format_container': '02unknownfileformat',
    'ready_files_container': '03readytoparse'
}
