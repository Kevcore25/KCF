# Version Changes
This list may not contain everything, but contains more detailed changes compared to the version highlights found in the KCF-Py file.
Typically the changes are KCF-Py. If it is original KCF, it will be mentioned.

A large version (V.2 > V.3 for example) is determined if the developer experience changes a lot, such as new functions or new ways to program.
A minor version (V.2.1 > V.2.2) is determined if it only adds minor changes or fixes bugs.

## V.2.3: Bug fixes
* Fixed incorrect p-numbers being added
* Changed the temp variable name for mulitple operations from temp# > .t-#
    * This is to prevent any mis-happenings that occur due to "temp#" player names
    * Additionally, the temp variables are essentially never to be used
* Updated examples/StaminaSystem.py for a better gameplay experience and explanations
* Minor other file changes

## V.2.0
+ More MC functions (e.g. setblock, give, effect)
+ Automatic variable declaration
+ Automatic custom commands implementation with triggers
# V.2.2
+ Accepts Decimals (up to 2 digits) for multiply and divide operations which round to the nearest int.