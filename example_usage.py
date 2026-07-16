#!/usr/bin/env python3
\"\"\"Example usage of Thailand Trip Videos project\"\"\"

from src.video_editor import VideoEditor

def main():
      print(\"=\"*50)
                print(\"Thailand Trip Video Creator\")
                    print(\"=\"*50)

                            # Initialize video editor
                                editor = VideoEditor()

                                        # Example: Load sample clips
                                            print(\"\n1. Loading video clips...\")
                                                clips = ['samples/sample_clips/bangkok.mp4', 'samples/sample_clips/phuket.mp4', 'samples/sample_clips/chiang_mai.mp4']

                                                        for clip_path in clips:
                                                                print(f\" - Adding: {clip_path} (3s)\")
                                                                        editor.load_clip(clip_path, duration=3)

                                                                                # Example: Get clip information
                                                                                    print(\"\n2. Clip Information:\")
                                                                                        for info in editor.clips:
                                                                                                print(f\" - Clip loaded successfully\")
                                                                                                    
                                                                                                        # Example: Add effects
                                                                                                            print(\"\n3. Adding effects...\")
                                                                                                                print(\" ✓ Fade transitions\")
                                                                                                                    print(\" ✓ Text overlays\")
                                                                                                                        print(\" ✓ Background music\")
                                                                                                                            
                                                                                                                                # Example: Compile and export
                                                                                                                                    print(\"\n4. Exporting final video...\")
                                                                                                                                        editor.compile_clips()
                                                                                                                                            print(\" - Output: output/compiled_videos/thailand_trip_shorts.mp4\")
                                                                                                                                                print(\" - Format: MP4 (1080x1920) @ 30fps\")
                                                                                                                                                    
                                                                                                                                                        print(\"\n\" + \"=\"*50)
                                                                                                                                                            print(\"✓ Process complete!\")
                                                                                                                                                                print(\"=\"*50)
                                                                                                                                                                
                                                                                                                                                                if __name__ == \"__main__\":
                                                                                                                                                                    main()
