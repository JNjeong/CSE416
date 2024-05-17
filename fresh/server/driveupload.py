from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

if __name__ == "__main__":
    try :
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()

    if not creds or creds.invalid:
        print("make new storage data file ")
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    # qgpt 키워드 가능
    FILES = (
        ('course_semester.xlsx'),
        ('courses.xlsx'),
        ('courses2.xlsx'),
        ('professors.xlsx'),
        ('qa.xlsx'),
        ('qgpt.xlsx')
    )

    for file_title in FILES :
        file_name = file_title
        metadata = {'name': file_name,
                    'mimeType': None
                    }

        res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
        if res:
            print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
            