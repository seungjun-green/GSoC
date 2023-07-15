import re
def file2List(fileName):
    res = set()
    with open(fileName, 'r') as f:
        all = f.readlines()
        for curr in all:
            res.add(curr)
    return res

def file2List2(fileName):
    res = []
    with open(fileName, 'r') as f:
        all = f.readlines()
        for curr in all:
            res.append(curr)
    return res


def saveList2FIle(fileName, data):
    with open(fileName, 'w') as f:
        for curr in data:
            f.write(curr)



def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()  # remove leading/trailing whitespace
            if line:  # ignore empty lines
                # remove starting number & dot using regex
                line = re.sub(r"^\d+\.\s*", "", line)
                outfile.write(line + '\n')






def combine_text_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in input_files:
            with open(file_name, 'r') as infile:
                outfile.write(infile.read())
            outfile.write('\n')


from google.cloud import storage
#
# def list_blobs(bucket_name):
#     """Lists all the blobs in the bucket."""
#     storage_client = storage.Client()
#
#     # Note: Client.list_blobs requires at least package version 1.17.0.
#     blobs = storage_client.list_blobs(bucket_name)
#     for blob in blobs:
#         print("ddd")
#         print(blob.name)
#
# list_blobs("gsoc_seungjunlee")

# client=storage.Client()
# bucket=client.get_bucket('gsoc_seungjunlee')
# blob=bucket.blob('GSoC_Dataset_final_V12.csv')
# blob.upload_from_filename('GSoC_Dataset_final_V12.csv')
