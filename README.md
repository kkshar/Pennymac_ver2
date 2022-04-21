# Pennymac_ver2

First, find what index does each header start (*):

  *   *      *      *      *       *     *         *    *     *
  |Dy |MxT   |MnT   |AvT   |HDDay  |AvDP |1HrP ... |MnR |AvSLP|
  |1  |88    |59    |74    |       |53.8 |         |23 1|004.5|
  |2  |79    |63    |71    |       |46.5 |         |28 1|004.5|
  |3  |77    |55    |66    |       |39.6 |         |24 1|016.8|
   ^                                   ^                     ^
   
       *                *      *     *    *     *       *      *
       |Team            |P     |W    |L   |D    |F      |A     |Pts
    1. |Arsenal         |38    |26   |9   |3    |79     |36    |87
    2. |Liverpool       |38    |24   |8   |6    |67     |30    |80
                          ...
   16. |Bolton          |38    | 9  1|3  1|6    |44     |62    |40
             ^                   ^    ^                          ^

Notice that the end index(^) of an entry is always in the index range of its header (not true for start index)

