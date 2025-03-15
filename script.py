import os
import subprocess

def get_video_resolution(file_path):
    """Mengambil resolusi video (width, height) menggunakan ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    width, height = map(int, result.stdout.strip().split(","))
    return width, height

def get_video_duration(file_path):
    """Mengambil durasi video dalam detik menggunakan ffmpeg."""
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(result.stdout.strip())

def split_video(file_path, output_folder):
    """Memotong video menjadi beberapa bagian dengan durasi 3 menit dan mengubah skala ke vertikal dengan posisi tengah."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    duration = get_video_duration(file_path)
    width, height = get_video_resolution(file_path)
    
    part_duration = 180  # 3 menit dalam detik
    total_parts = int(duration // part_duration) + (1 if duration % part_duration > 0 else 0)
    
    # Menyesuaikan video ke format vertikal TikTok (1080x1920) tanpa distorsi
    if width > height:  # Landscape (1280x720)
        vf_base = "scale=1080:-2,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black"
    else:  # Portrait atau hampir vertikal
        vf_base = "scale=-2:1920,crop=1080:1920"
    
    # Meminta judul video dari pengguna
    video_title = input("Masukkan judul video: ")
    
    for i in range(total_parts):
        start_time = i * part_duration
        output_file = os.path.join(output_folder, f"part_{i+1}.mp4")
        
        # Menambahkan teks overlay untuk judul (di atas) dan nomor part (di bawah)
        vf_text = (
    f"drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':text='Follow untuk lebih banyak konten!':fontcolor=red:fontsize=40:x=(w-text_w)/2:y=h-580,"
    f"drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':text='{video_title}':fontcolor=yellow:fontsize=60:x=(w-text_w)/2:y=500,"
    f"drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':text='Part {i+1}':fontcolor=orange:fontsize=70:x=(w-text_w)/2:y=h-500"
)
        
        vf_filter = f"{vf_base},{vf_text}"
        
        cmd = [
            "ffmpeg", "-i", file_path,
            "-vf", vf_filter,
            "-ss", str(start_time), "-t", str(part_duration),
            "-c:v", "libx264", "-crf", "23", "-preset", "fast",
            "-c:a", "aac", "-b:a", "128k",
            output_file
        ]
        
        print(f"Memproses bagian {i+1}...")
        subprocess.run(cmd)
        
    print("Selesai!")

if __name__ == "__main__":
    input_file = input("Masukkan nama file mp4: ")
    output_folder = input("Masukkan nama folder hasil: ")
    
    split_video(input_file, output_folder)
