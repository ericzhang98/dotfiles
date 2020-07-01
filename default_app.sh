# https://chainsawonatireswing.com/2012/09/19/changing-default-applications-on-a-mac-using-the-command-line-then-a-shell-script/
{ cat <<eof
com.apple.TextEdit:py
com.apple.TextEdit:cpp
com.apple.TextEdit:c
com.apple.TextEdit:h
com.apple.TextEdit:m
com.apple.TextEdit:md
com.apple.TextEdit:json
com.apple.TextEdit:js
com.apple.TextEdit:ts
com.apple.TextEdit:rb
com.apple.TextEdit:java
com.apple.TextEdit:hs
eof
} | grep . |
while IFS=$':' read bundle_id extension ; do
  # Grep to see if Bundle ID exists, sending stdout to /dev/null
  /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep $bundle_id > /dev/null  
  # Save exit status (0=success & 1=failure)
  status=$?
  # If exit status failed, notify me & exit; if not, change default app for extension
  if test $status -eq 1 ; then
    echo "$bundle_id doesn't exist! Fix the script!"
    exit
  else
    echo "\nChanging $extension so it opens with $bundle_id …\n"
    duti -s $bundle_id .$extension all
    echo "Here's proof…\n"
    duti -x $extension
    echo "\n----------"
  fi
done
