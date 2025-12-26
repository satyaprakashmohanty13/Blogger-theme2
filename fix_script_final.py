
import sys

try:
    with open('theme-6143575791238606864.xml', 'r') as f:
        content = f.read()

    # The broken function currently in the file (based on previous print)
    # The start marker is the same.
    start_marker = 'Lt=async(e,t=20,a="published",l=!1,s=!1,i=!1)=>{'
    end_marker = 'return c.posts.length>t&&c.posts.splice(t),c}}}return null},'

    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Start marker not found")
        sys.exit(1)

    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print("End marker not found")
        sys.exit(1)

    full_match = content[start_idx : end_idx + len(end_marker)]
    print(f"Found block of length {len(full_match)}")

    # Correct function with correct escaping for Python string

    correct_lt = r'''Lt=async(e,t=20,a="published",l=!1,s=!1,i=!1)=>{let labels=e.split(",").map(l=>l.trim()).filter(l=>l);let n=0;if(labels.length>1){for(let lbl of labels){n+=vt(lbl)}}else{n=vt(e)}if(e&&n>0){let r=s&&!!ae.c&&ae.c.lab.includes(e),o=r?t+1:t,d=l&&n>o?$e.floor($e.random()*(n-o+1)):0;if(r?n>=2:n>=1){let l,s=Ee(se.cnHmU),n=s.searchParams;if(labels.length>1){l=!1;s.pathname="/search";let q=labels.map(lbl=>`label:"${lbl}"`).join(" OR ");n.set("q",q)}else{0===d||e.includes("|")||e.includes('"')?(l=!0,s.pathname=`/search/label/${xe(e)}`):(l=!1,s.pathname="/search",/\s/.test(e)?n.set("q",`label:"${e}"`):n.set("q",`label:${e}`))}n.set("m","0"),n.set("view","x-content-blog"),n.set("max-results",me(o)),n.set("sort-by",a),n.set("by-date",me("published"===a||"updated"===a)),n.set("start",me(d));let c=await ft(s,a,i);if(c){if(r&&se.siId&&(c.elements=c.elements.filter(e=>!_(e,"data-id")||E(e,"data-id")!==se.siId),c.posts=c.posts.filter(e=>e.id!==se.siId)),c.elements.length>t){let e=c.elements.filter(e=>"article"===e.tagName.toLowerCase());("updated"===a||(l?"published"!==a:"published"===a)||e.length>t)&&(e.length>t&&e.splice(t),c.elements=e)}return c.posts.length>t&&c.posts.splice(t),c}}}return null},'''

    new_content = content.replace(full_match, correct_lt)

    with open('theme-6143575791238606864.xml', 'w') as f:
        f.write(new_content)

    print("Successfully corrected Lt function.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
