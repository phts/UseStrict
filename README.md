# UseStrict

[![Package Control](https://img.shields.io/packagecontrol/dt/UseStrict.svg)](https://packagecontrol.io/packages/UseStrict)

Package for Sublime Text 3.
Insert "use strict" directive to the top of the file.

## Install

**Via Package Control**:

Open Command Palette &rarr; `Package Control: Install Package` &rarr; `UseStrict`

## Usage

Run command `UseStrict: Insert "use strict" to the top of the file` and
it will append `'use strict'` to the top of the active file.

## Settings

```js
{
  // Whether to insert semicolon after the "use strict" directive
  "semicolon": false,

  // String quote symbol to use in the "use strict" directive. Can be "'", "\"" or even any string.
  "quote_symbol": "'",
}
```
