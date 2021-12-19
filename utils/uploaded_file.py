from django.core.files.uploadedfile import SimpleUploadedFile


def fake_uploaded_file(file_path, mime_type):
    with open(file_path, 'rb') as fh:
        suf = SimpleUploadedFile(file_path.split('/')[-1], fh.read(), mime_type)
        suf.seek(0)
        return suf
