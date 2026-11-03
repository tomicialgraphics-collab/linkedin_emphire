#!/bin/sh
set -e

convert -size 1584x396 xc:'#0B1E14' -fill '#2FBF71' -draw "rectangle 0,0 8,396" \
 -font DejaVu-Sans-Bold -pointsize 50 -fill '#FFFFFF' -annotate +430+142 "Most AI failures ship\nwith a green dashboard." \
 -font DejaVu-Sans -pointsize 25 -fill '#9FB3A8' -annotate +430+300 "Red teaming and evaluations that end in a\nreproducible finding, not a screenshot." \
 banner_A_green-dashboard.png

convert -size 1584x396 xc:'#0B1E14' -fill '#2FBF71' -draw "rectangle 0,0 8,396" \
 -font DejaVu-Sans-Bold -pointsize 52 -fill '#FFFFFF' -annotate +430+142 "I find the failures\nbenchmarks miss." \
 -font DejaVu-Sans -pointsize 25 -fill '#9FB3A8' -annotate +430+300 "Red teaming and reproducible evaluation for\nagents with tools, data and permissions." \
 banner_B_benchmarks-miss.png

convert -size 1584x396 xc:'#0B1E14' -fill '#2FBF71' -draw "rectangle 0,0 8,396" \
 -font DejaVu-Sans-Bold -pointsize 42 -fill '#FFFFFF' -annotate +430+138 "Your agent has tools, data\nand permissions. I test what\nhappens when someone pushes." \
 -font DejaVu-Sans -pointsize 25 -fill '#9FB3A8' -annotate +430+300 "Before launch, not after. A second pair of\neyes on the checks you already trust." \
 -font DejaVu-Sans-Bold -pointsize 18 -fill '#2FBF71' -annotate +430+372 "DM me   ·   Lagos, Nigeria" \
 banner_C_your-agent.png

convert -size 1584x396 xc:'#0B1E14' -fill '#2FBF71' -draw "rectangle 0,0 8,396" \
 -font DejaVu-Sans-Bold -pointsize 44 -fill '#FFFFFF' -annotate +430+152 "AI security and evaluations" \
 -font DejaVu-Sans -pointsize 25 -fill '#9FB3A8' -annotate +430+300 "Agents, retrieval, tool permissions.\nFindings published with the evidence." \
 banner_D_quiet.png
