# Version Changes
This list may not contain everything, but contains more detailed changes compared to the version highlights found in the KCF-Py file.
Typically the changes are KCF-Py. If it is original KCF, it will be mentioned.

A large version (V.2 > V.3 for example) is determined if the developer experience changes a lot, such as new functions or new ways to program.
A minor version (V.2.1 > V.2.2) is determined if it only adds minor changes or fixes bugs.

## V.3.0: New f-string system!
* Forced all function names to be lowered
* "Function" type now accepts both a function name, or a function call
    * A lambda expression also may be accepted but it is buggy. Don't use the lambda expression if you do not need it.
* Optimized if statements: If the result is only one expression, a function is not created
* "or" condition still does not work as expected but it is possible as long as:
    * the or condition is the last in the conditional statement and there is no "and" after it
    * e.g. (x and y or b) works but (x and y or b and y) does not
    * in general, the or operation is very buggy and should not be used
* Added KTF (FormattedString) support! Finally! See tellraw & title functions and documentation for how to use.
* Added a bunch of commonly used commands. Other commands may still be ran using the RUN function
    * Notice: A lot of these "commonly used commands" are built with the intent of shortcuts. 
    * For example, tellraw and title uses its own f-string interpreter
    * Many commands which I see to have no shortcuts are not implemented and you can just use the RUN function
* Fixed negative integers from breaking the code
* Many other bug fixes

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
## V.2.2
+ Accepts Decimals (up to 2 digits) for multiply and divide operations which round to the nearest int.