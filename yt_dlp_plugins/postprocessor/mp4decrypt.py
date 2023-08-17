from yt_dlp.postprocessor.common import PostProcessor
import os
import subprocess

class MP4DecryptPP(PostProcessor):
    def __init__(self, downloader=None, **kwargs):
        super().__init__(downloader)
        self._kwargs = kwargs

    def run(self, info):
        filepath = info.get('filepath')
        if filepath:
            decrypted_filepath = self.decrypt_file(filepath)
            if decrypted_filepath:
                decryption_key = self._kwargs.get('key', [])
                if 'keyfile' in self._kwargs:
                    self.to_screen(f'Decryption successful for {filepath!r} with keyfile: {self._kwargs["keyfile"]}')
                else:
                    self.to_screen(f'Decryption successful for {filepath!r} with key: {decryption_key}')
                os.remove(filepath)
                os.rename(decrypted_filepath, filepath)
            else:
                decryption_key = self._kwargs.get('key', [])
                if 'keyfile' in self._kwargs:
                    self.to_screen(f'Decryption failed for {filepath!r} with keyfile: {self._kwargs["keyfile"]}')
                else:
                    self.to_screen(f'Decryption failed for {filepath!r} with key: {decryption_key}')
        else:
            filepath = info.get('_filename')
            self.to_screen(f'Pre-processed {filepath!r} with {self._kwargs}')
        return [], info

    def decrypt_file(self, filepath):
        decryption_key = self._kwargs.get('key', [])
        keys_file = self._kwargs.get('keyfile')
        
        if keys_file and not decryption_key:
            if os.path.exists(keys_file):
                with open(keys_file) as f:
                    keys = f.read().splitlines()
            else:
                raise FileNotFoundError(f"Key file '{keys_file}' not found.")
        elif decryption_key and not keys_file:
            keys = [decryption_key]
        else:
            return None
        
        output_file = f"{os.path.splitext(filepath)[0]}_decrypted{os.path.splitext(filepath)[1]}"
        try:
            cmd = ["mp4decrypt"]
            for key in keys:
                cmd.extend(["--key", key])
            cmd.extend([filepath, output_file])
            subprocess.run(cmd, check=True)
            return output_file
        except subprocess.CalledProcessError:
            return None

def setup(downloader, **kwargs):
    downloader.add_post_processor(MP4DecryptPP(downloader, **kwargs))
