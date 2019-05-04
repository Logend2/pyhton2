from qiniu import Auth, put_file, etag
import qiniu.config
access_key = 'gbd8YrpRrZ3UOCCEoXz28W21OnX6eS2utYtRow6l'
secret_key = 'Y3CbwZC_ODovvs-HAIxSlYfbMwSEYL7yMLyy26-I'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'xgmm'
#上传后保存的文件名
localfile = input('输入上传文件名:\n')
key = input(''.join(['保存文件名(',localfile,')']))
if key == '':
    key = localfile
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径

ret, info = put_file(token, key, localfile)
print(info)
if str(info).find('200') != -1:
    print('上传成功')
else:
    prin('上传失败')
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
input('按任意键退出')
