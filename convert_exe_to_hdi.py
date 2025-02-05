# convert_exe_to_hdi.py

import os

def convert_exe_to_hdi(exe_file, hdi_file):
    # ここにEXEからHDIへの変換ロジックを追加します
    # 例: ファイルをコピーするだけの仮の処理
    with open(exe_file, 'rb') as f:
        data = f.read()

    with open(hdi_file, 'wb') as f:
        f.write(data)

    print(f'Converted {exe_file} to {hdi_file}')

if __name__ == "__main__":
    exe_file = 'PLUS_DISC.exe'
    hdi_file = 'output.hdi'
    convert_exe_to_hdi(exe_file, hdi_file)
