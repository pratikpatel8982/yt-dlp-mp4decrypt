```markdown
# yt-dlp MP4Decrypt Plugin

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![yt-dlp Version](https://img.shields.io/badge/yt--dlp-2021.09.06%2B-blue.svg)

This is a plugin for yt-dlp that enables decryption of encrypted MP4 files using the `mp4decrypt` command-line tool.

## Installation

You can install this plugin directly from the GitHub repository using the following command:

```bash
python -m pip install -U https://github.com/pratikpatel8982/yt-dlp-mp4decrypt/archive/master.zip
```

Make sure you have Python 3.6+ installed before running this command.

## Usage

To use this plugin, you can pass the `--use-post-processor` option along with the `MP4Decrypt` plugin name and the required arguments.

### Decrypt using a single key:

```bash
yt-dlp --use-post-processor MP4Decrypt:key=your_key <video_url>
```

Replace `your_key` with your actual decryption key.

### Decrypt using keys from a file:

```bash
yt-dlp --use-post-processor MP4Decrypt:keyfile="/path/to/keys.txt" <video_url>
```

Replace `/path/to/keys.txt` with the actual path to your keys file. Make sure `keys.txt` contains keys in the format `kid:key`, one per line.
