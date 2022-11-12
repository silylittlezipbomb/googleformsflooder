# googleformsflooder
This program allows you to add mass amounts of submissions to a Google Form. This causes rate limits after a while if you go higher than about 3 threads, and I don't currently plan on adding proxy support.
I managed to get to 100k submissions without being rate limited using 2 threads.

## How to use
Go to the form you'd like to use, and fill out all the information with the inspector and open the network tab. Submit the form, open formResponse and all the data is there. 
The keys should be formatted like "entry.xxxxxxxxxx" 
