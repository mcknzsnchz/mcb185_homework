   O
Z     N
   R
I     C
   A
   
  gunzip -c dictionary.gz | grep -E "r+[oncainzr]{3,}" | grep -v "[bdefghjklmpqstuvwxy]" | wc -l
  gunzip -c dictionary.gz | grep -E "r+[oncainzr]" | grep -v "[bdefghjklmpqstuvwxy]" | wc -l

I was able to get 32. 
I see that for every "r" that does not end a word, there are at least 3 other characters following. 
I know that if I do not include the {3,} bound, there are more words like "zori" and "orca" which would only have {1,} or {2,}.
If I add a second grep it does not allow me to join the two on one line to where it includes "r" with 3 letters after and "r" with 1 or 2.
I do not know how to get it to where the word itself is 4 or more letters.