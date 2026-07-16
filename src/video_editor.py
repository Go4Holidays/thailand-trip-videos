import os
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip

class VideoEditor:
      """Main video editor class for compiling Thailand trip videos"""

    def __init__(self, config_path='config/settings.json'):
              """Initialize video editor with config settings"""
              with open(config_path, 'r') as f:
                            self.config = json.load(f)
                        self.clips = []
        self.compiled_video = None
        self._ensure_output_dir()

    def _ensure_output_dir(self):
              """Create output directory if it doesn't exist"""
        os.makedirs('output/compiled_videos', exist_ok=True)

    def load_clip(self, clip_path, duration=None):
              """Load a video clip"""
        try:
                      clip = VideoFileClip(clip_path)
                      if duration:
                                        clip = clip.subclipped(0, duration)
                                    self.clips.append(clip)
            print(f"✓ Loaded: {clip_path}")
            return clip
except Exception as e:
            print(f"✗ Error loading : {clip_path} - {e}")

    def add_text_overlay(self, text, position='center', duration=None):
              """Add text overlay to current clip"""
        if not self.clips:
                      print("No clips loaded")
            return
        txt_clip = TextClip(text, fontsize=70, color='white', font='Arial-Bold')
        return txt_clip

    def compile_clips(self):
              """Compile all loaded clips into single video"""
        if not self.clips:
                      print("No clips to compile")
            return
        self.compiled_video = concatenate_videoclips(self.clips)
        return self.compiled_video

    def add_music(self, audio_path):
              """Add background music to video"""
        print(f"Adding music from: {audio_path}")
        # Music integration logic here
        pass

    def export(self, output_filename='thailand_trip.mp4', fps=30):
              """Export final video"""
        if not self.compiled_video:
                      print("No compiled video to export")
            return
        output_path = f"output/compiled_videos/{output_filename}"
        self.compiled_video.write_videofile(output_path, fps=fps, verbose=False, logger=None)
        print(f"✓ Video exported successfully!")
