# youtube-captioning
Youtube can auto generate subtitles. It has a perfect timing. But sometimes, it has some error. We can update the transcripts if it is the our own video. If it is someone else’s, it is not allowed to edit in the Youtube. [Amara](www.amara.org) is a great website that makes it possible to edit the subtitles of youtube videos. It generates a new subtitles on top of the original one. All you need is copy the embed code from Amara and insert into your websites. It seems a great way to edit the youtube captioning. However, we have following problems if we take this method to edit youtube transcripts.
 - Amara need a SRT file to start with. So we have to download the SRT file from Youtube. We can use www.ccsubs.com to get the SRT file from Youtube. We can upload the SRT file to Amara.
 - But we ends up having a messy timing sync in Amara. So we have to solve to timing problem in addition to the work of editing the transcripts.

I have come up with my own solution to the above problems. My solution takes following steps:
 1. Download the timedtext xml file from Youtube.
 2. Convert the xml into the srt file.
 3. Solve the timing problem.

## Dependencies
 - python2.7 64
 - pip install beautifulsoup4
 - pip install glob
## Guide
### Download the timedtext xml file from Youtube
   - Open the youtube video in the Chrome. Right click, select ‘Inspect’.
   - Click ‘Network’ tab, shown in bellow.
   - Then click the ‘cc’ in the youtube video
   - You will see new generated lines in the Network tab. Choose one start with ‘timedtext?’ and right click and  ‘Open link in new tab’.
   - We can see the xml file now. We just need to ‘save as’ this page into you local computer. This is the xml file we are going to use in our next step.
### Convert the xml into the srt file
python xml2srt.py [xml-file1] [xml-file2] [xml-file3] …

### Solve the timing problem
python srt2std.py [srt-file1] [srt-file2] [srt-file3] …

Now, we can upload these srt files into Amara, and start editing the transcripts. Timing sync is perfect now. You just need to correct some of the words that are incorrectly captioned by Youtube machine. After finish editing the transcript, we just need to copy the embed code from Amara, and then insert the embed code into the website html you prefer.

Please see more detailed guid in [this blog](https://mdalaiblog.wordpress.com/2017/05/15/a-way-to-edit-youtube-auto-captioning/).
