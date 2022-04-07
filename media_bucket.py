import os # to save recording to disk
from flask import request
import boto3

BUCKET_PREFIX = "330-personal-test-bucket"
# Replace above with "ucm-cse-120-330-" when credentials are given.

def get_media(media_got):
    print("Media bucket script")
    print(media_got)
    audio_to_write=media_got.read()
    #write to server folder
    f = open('./Audios/test.wav', 'wb')
    #f.write(request.get_data("audio_data"))
    f.write(audio_to_write)
    f.close()

    return 1


def get_language(key: str):
    """Finds language using given key. Used to select bucket when downloading."""
    lang = key[3, 5]
    if lang == "eng":
        return "english"
    elif lang == "can":
        return "cantonese"
    elif lang == "man":
        return "mandarin"
    elif lang == "spa":
        return "spanish"
    else:
        return "tagalog"


def aws_upload(file_key: str, file_to_upload: str, language: str):
    """Uploads a file to an AWS bucket.

    Arguments:

        file_key: This should be the name you want the file saved under on AWS.
        AWS doesn't just use the given file name. PLEASE MAKE SURE IT ENDS IN .WAV!

        file_to_upload: Actual (local) path of the file to be uploaded.

        language: Bucket to shove it in. Buckets follow the same naming convention, so all you need to input is the
        language of the file.
    """
    aws_client = boto3.client('s3')
    aws_client.upload_file(file_to_upload, BUCKET_PREFIX, file_key)
    # aws_client.upload_file(file_to_upload, "ucm-cse-120-330-" + language, file_key) <<UNCOMMENT WHEN AWS SHIT HITS


def aws_download(file_key: str):
    """Returns an AWS url that allows file downloads for an hour.

    Arguments:

        file_key: Name of the file on AWS. Also known as the key used when you called aws_upload.
    """
    language = get_language(file_key)
    url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': BUCKET_PREFIX, 'Key': file_key},
        ExpiresIn=3600)
    # url = boto3.client('s3').generate_presigned_url(
    #     ClientMethod='get_object',
    #     Params={'Bucket': BUCKET_PREFIX + language, 'Key': file_key},
    #     ExpiresIn=3600) << Replace above with this when school account is active!
    return url


def aws_batch_download(file_keys):
    """Generates a zip file containing requested files. Uploads to AWS.
    Returns the AWS url of the generated zip file.

    Arguments:

        file_keys: List/Set/Whatever of file keys.
    """
    aws_client = boto3.client('s3')
    for key in file_keys:  # Downloads all selected files to local directory.
        aws_client.download_file(BUCKET_PREFIX, key, "temp_download/batch/" + key)
        # lang = get_language(key)
        # aws_client.download_file(BUCKET_PREFIX + lang, key, "temp_download/batch/" + key) << see above comments
    import shutil, os
    zip_file_name = "testarchive"
    shutil.make_archive(zip_file_name, 'zip', "temp_download/")  # Zip 'em up.
    aws_client.upload_file(zip_file_name + ".zip", BUCKET_PREFIX, zip_file_name + ".zip")  # Upload it.
    url = aws_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': BUCKET_PREFIX, 'Key': zip_file_name},
        ExpiresIn=3600)
    for file in os.scandir("temp_download/batch/"):
        os.remove(file.path)
    return url