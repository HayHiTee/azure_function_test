from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def upload_file_to_storage(file_to_upload, connection_string, container_name):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_to_upload)

    with open(file_to_upload, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)



def download_file_from_storage(download_location_path_name, blob_to_download, connection_string, container_name):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_to_download)

    with open(download_location_path_name, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())


