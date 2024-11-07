import os
import subprocess
import glob

# 用户输入要处理的文件夹路径
directory_path = input("请输入要处理的文件夹路径: ")

# 定义支持的视频文件扩展名
extensions = ('.mkv', '.avi', '.usm', '.wmv', '.moflex', '.m4v', '.mpg', '.webm', '.bik', '.3gp', '.flv', '.vob', '.ogv', '.thp' ,'.pss')

def is_valid_path(path):
    """检查路径是否指向一个有效的文件"""
    return os.path.isfile(path)

def convert_video_to_mp4(input_file):
    """使用ffmpeg将视频文件转换为MP4格式"""
    output_file = os.path.splitext(input_file)[0] + '.mp4'
    try:
        subprocess.run([
            'ffmpeg', '-i', input_file, '-c:v', 'libx265', '-b:v', '20M', '-r', '60', '-crf', '16', '-preset', 'fast',
            '-vf', 'scale=2048:1080', '-c:a', 'aac', '-b:a', '1536k', output_file
        ], check=True)
        print(f'Converted video: {input_file} to {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Failed to convert {input_file}: {e}')

# 初始化转换计数
conversion_count = 0

# 确保输入的路径存在
if os.path.isdir(directory_path):
    # 遍历用户指定的目录及所有子目录
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # 构建完整的文件路径
            file_path = os.path.join(root, file)
            
            # 检查文件扩展名是否是我们支持的格式
            if file.lower().endswith(extensions) and is_valid_path(file_path):
                conversion_count += 1
                print(f'Processing ({conversion_count}/{len(files)}): {file_path}')
                convert_video_to_mp4(file_path)
else:
    print(f'Error: 指定的路径 "{directory_path}" 不是一个有效的目录。')

# 输出转换完成的文件数
print(f'Conversion completed for {conversion_count} files.')

# 退出脚本
sys.exit()
