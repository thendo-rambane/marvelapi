# Possible Search parameters

This is a comprehensive list of all possible search parameters and their types

## characters

### name

#### Return only characters matching the specified full character name (e.g. Spider-Man).

    * type: string

    * Allowed values:

        * : any string

### nameStartsWith

#### Return characters with names that begin with the specified string (e.g. Sp).

    * type: string

    * Allowed values:

        * : any string

### modifiedSince

#### Return only characters which have been modified since the specified date.

    * type: Date

    * Allowed values:

        * : any Date

### comics

#### Return only characters which appear in the specified comics (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### series

#### Return only characters which appear the specified series (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### events

#### Return only characters which appear in the specified events (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### stories

#### Return only characters which appear the specified stories (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### orderBy

#### Order the result set by a field or fields. Add a "-" to the value sort in descending order. Multiple values are given priority in the order in which they are passed.

    * type: list of string

    * Allowed values:

        * name

        * modified

        * -name

        * -modified

### limit

#### Limit the result set to the specified number of resources.

    * type: int

    * Allowed values:

        * : any Any number from 1 to 100

### offset

#### Skip the specified number of resources in the result set.

    * type: int

    * Allowed values:

        * : any int

## comics

### format

#### Filter by the issue format (e.g. comic, digital comic, hardcover).

    * type: string

    * Allowed values:

        * comic

        * magazine

        * trade paperback

        * hardcover

        * digest

        * graphic novel

        * digital comic

        * infinite comic

### formatType

#### Filter by the issue format type (comic or collection).

    * type: string

    * Allowed values:

        * comic

        * collection

### noVariants

#### Exclude variants (alternate covers, secondary printings, director's cuts, etc.) from the result set.

    * type: boolean

    * Allowed values:

        * true

### dateDescriptor

#### Return comics within a predefined date range.

    * type: string

    * Allowed values:

        * lastWeek

        * thisWeek

        * nextWeek

        * thisMonth

### dateRange

#### Return comics within a predefined date range.  Dates must be specified as date1,date2 (e.g. 2013-01-01,2013-01-02).  Dates are preferably formatted as YYYY-MM-DD but may be sent as any common date format.

    * type: list of int

    * Allowed values:

        * : any list of int

### title

#### Return only issues in series whose title matches the input.

    * type: string

    * Allowed values:

        * : any string

### titleStartsWith

#### Return only issues in series whose title starts with the input.

    * type: string

    * Allowed values:

        * : any string

### startYear

#### Return only issues in series whose start year matches the input.

    * type: int

    * Allowed values:

        * : any int

### issueNumber

#### Return only issues in series whose issue number matches the input.

    * type: int

    * Allowed values:

        * : any int

### diamondCode

#### Filter by diamond code.

    * type: string

    * Allowed values:

        * : any string

### digitalId

#### Filter by digital comic id.

    * type: int

    * Allowed values:

        * : any int

### upc

#### Filter by UPC.

    * type: string

    * Allowed values:

        * : any string

### isbn

#### Filter by ISBN.

    * type: string

    * Allowed values:

        * : any string

### ean

#### Filter by EAN.

    * type: string

    * Allowed values:

        * : any string

### issn

#### Filter by ISSN.

    * type: string

    * Allowed values:

        * : any string

### hasDigitalIssue

#### Include only results which are available digitally.

    * type: boolean

    * Allowed values:

        * true

### modifiedSince

#### Return only comics which have been modified since the specified date.

    * type: Date

    * Allowed values:

        * : any Date

### creators

#### Return only comics which feature work by the specified creators (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### characters

#### Return only comics which feature the specified characters (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### series

#### Return only comics which are part of the specified series (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### events

#### Return only comics which take place in the specified events (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### stories

#### Return only comics which contain the specified stories (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### sharedAppearances

#### Return only comics in which the specified characters appear together (for example in which BOTH Spider-Man and Wolverine appear). Accepts a comma-separated list of ids.

    * type: list of int

    * Allowed values:

        * : any list of int

### collaborators

#### Return only comics in which the specified creators worked together (for example in which BOTH Stan Lee and Jack Kirby did work). Accepts a comma-separated list of ids.

    * type: list of int

    * Allowed values:

        * : any list of int

### orderBy

#### Order the result set by a field or fields. Add a "-" to the value sort in descending order. Multiple values are given priority in the order in which they are passed.

    * type: list of string

    * Allowed values:

        * focDate

        * onsaleDate

        * title

        * issueNumber

        * modified

        * -focDate

        * -onsaleDate

        * -title

        * -issueNumber

        * -modified

### limit

#### Limit the result set to the specified number of resources.

    * type: int

    * Allowed values:

        * : any Any number from 1 to 100

### offset

#### Skip the specified number of resources in the result set.

    * type: int

    * Allowed values:

        * : any int

## creators

### firstName

#### Filter by creator first name (e.g. Brian).

    * type: string

    * Allowed values:

        * : any string

### middleName

#### Filter by creator middle name (e.g. Michael).

    * type: string

    * Allowed values:

        * : any string

### lastName

#### Filter by creator last name (e.g. Bendis).

    * type: string

    * Allowed values:

        * : any string

### suffix

#### Filter by suffix or honorific (e.g. Jr., Sr.).

    * type: string

    * Allowed values:

        * : any string

### nameStartsWith

#### Filter by creator names that match critera (e.g. B, St L).

    * type: string

    * Allowed values:

        * : any string

### firstNameStartsWith

#### Filter by creator first names that match critera (e.g. B, St L).

    * type: string

    * Allowed values:

        * : any string

### middleNameStartsWith

#### Filter by creator middle names that match critera (e.g. Mi).

    * type: string

    * Allowed values:

        * : any string

### lastNameStartsWith

#### Filter by creator last names that match critera (e.g. Ben).

    * type: string

    * Allowed values:

        * : any string

### modifiedSince

#### Return only creators which have been modified since the specified date.

    * type: Date

    * Allowed values:

        * : any Date

### comics

#### Return only creators who worked on in the specified comics (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### series

#### Return only creators who worked on the specified series (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### events

#### Return only creators who worked on comics that took place in the specified events (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### stories

#### Return only creators who worked on the specified stories (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### orderBy

#### Order the result set by a field or fields. Add a "-" to the value sort in descending order. Multiple values are given priority in the order in which they are passed.

    * type: list of string

    * Allowed values:

        * lastName

        * firstName

        * middleName

        * suffix

        * modified

        * -lastName

        * -firstName

        * -middleName

        * -suffix

        * -modified

### limit

#### Limit the result set to the specified number of resources.

    * type: int

    * Allowed values:

        * : any Any number from 1 to 100

### offset

#### Skip the specified number of resources in the result set.

    * type: int

    * Allowed values:

        * : any int

## events

### name

#### Return only events which match the specified name.

    * type: string

    * Allowed values:

        * : any string

### nameStartsWith

#### Return events with names that begin with the specified string (e.g. Sp).

    * type: string

    * Allowed values:

        * : any string

### modifiedSince

#### Return only events which have been modified since the specified date.

    * type: Date

    * Allowed values:

        * : any Date

### creators

#### Return only events which feature work by the specified creators (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### characters

#### Return only events which feature the specified characters (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### series

#### Return only events which are part of the specified series (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### comics

#### Return only events which take place in the specified comics (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### stories

#### Return only events which take place in the specified stories (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### orderBy

#### Order the result set by a field or fields. Add a "-" to the value sort in descending order. Multiple values are given priority in the order in which they are passed.

    * type: list of string

    * Allowed values:

        * name

        * startDate

        * modified

        * -name

        * -startDate

        * -modified

### limit

#### Limit the result set to the specified number of resources.

    * type: int

    * Allowed values:

        * : any Any number from 1 to 100

### offset

#### Skip the specified number of resources in the result set.

    * type: int

    * Allowed values:

        * : any int

## series

### title

#### Return only series matching the specified title.

    * type: string

    * Allowed values:

        * : any string

### titleStartsWith

#### Return series with titles that begin with the specified string (e.g. Sp).

    * type: string

    * Allowed values:

        * : any string

### startYear

#### Return only series matching the specified start year.

    * type: int

    * Allowed values:

        * : any int

### modifiedSince

#### Return only series which have been modified since the specified date.

    * type: Date

    * Allowed values:

        * : any Date

### comics

#### Return only series which contain the specified comics (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### stories

#### Return only series which contain the specified stories (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### events

#### Return only series which have comics that take place during the specified events (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### creators

#### Return only series which feature work by the specified creators (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### characters

#### Return only series which feature the specified characters (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### seriesType

#### Filter the series by publication frequency type.

    * type: string

    * Allowed values:

        * collection

        * one shot

        * limited

        * ongoing

### contains

#### Return only series containing one or more comics with the specified format.

    * type: list of string

    * Allowed values:

        * comic

        * magazine

        * trade paperback

        * hardcover

        * digest

        * graphic novel

        * digital comic

        * infinite comic

### orderBy

#### Order the result set by a field or fields. Add a "-" to the value sort in descending order. Multiple values are given priority in the order in which they are passed.

    * type: list of string

    * Allowed values:

        * title

        * modified

        * startYear

        * -title

        * -modified

        * -startYear

### limit

#### Limit the result set to the specified number of resources.

    * type: int

    * Allowed values:

        * : any Any number from 1 to 100

### offset

#### Skip the specified number of resources in the result set.

    * type: int

    * Allowed values:

        * : any int

## stories

### modifiedSince

#### Return only stories which have been modified since the specified date.

    * type: Date

    * Allowed values:

        * : any Date

### comics

#### Return only stories contained in the specified (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### series

#### Return only stories contained the specified series (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### events

#### Return only stories which take place during the specified events (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### creators

#### Return only stories which feature work by the specified creators (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### characters

#### Return only stories which feature the specified characters (accepts a comma-separated list of ids).

    * type: list of int

    * Allowed values:

        * : any list of int

### orderBy

#### Order the result set by a field or fields. Add a "-" to the value sort in descending order. Multiple values are given priority in the order in which they are passed.

    * type: list of string

    * Allowed values:

        * id

        * modified

        * -id

        * -modified

### limit

#### Limit the result set to the specified number of resources.

    * type: int

    * Allowed values:

        * : any Any number from 1 to 100

### offset

#### Skip the specified number of resources in the result set.

    * type: int

    * Allowed values:

        * : any int

