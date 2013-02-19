# ”Undo Selected Lines“ for Sublime Text 2

This is a small command that overrides the default “soft undo“ when you're going to undo the added lines (carets). The default behavior is to undo all the added carets in one go, so it's almost always unusable.

This problem bugged me for some time, but when I saw it [bugged someone else](http://stackoverflow.com/q/14677311/885556), I've created this small command.

Known issue: there is no “soft redo” available after this command (and the history is dirty), I couldn't find a way not to put the command into history (when doing in always faulty context the selection is not updated visually in ST), so if you could improve it — Pull Requests would be cool.