import boto3
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})

@application.route('/')
def main():
    return "hello bt4221"

@application.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']
    s3 = boto3.client('s3',
                      aws_access_key_id=os.environ["AKIAUDDHJRB5TJKADXIH"],
                      aws_secret_access_key=os.environ["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"]
                      )
    s3.put_object(
        ACL="public-read",
        Bucket=os.environ["mybt4221"],
        Body=file,
        Key=file.filename,
        ContentType=file.content_type
    )
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    application.debug = True
    application.run()