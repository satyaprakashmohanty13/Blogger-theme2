
import sys

try:
    with open('theme-6143575791238606864.xml', 'r') as f:
        content = f.read()

    # --- Step 1: Update xt to bypass count check if comma is present ---
    # The current string in xt:
    # vt(o)?$t(e,async()=>{try{let e=await Lt(o,c,h,g,!1,p);e&&e.elements.length?l(e.elements,e.dom):s()}catch(e){i(e)}}):s()

    search_xt = 'vt(o)?$t(e,async()=>{try{let e=await Lt(o,c,h,g,!1,p);e&&e.elements.length?l(e.elements,e.dom):s()}catch(e){i(e)}}):s()'
    replace_xt = '(vt(o)||o.includes(","))?$t(e,async()=>{try{let e=await Lt(o,c,h,g,!1,p);e&&e.elements.length?l(e.elements,e.dom):s()}catch(e){i(e)}}):s()'

    if search_xt in content:
        content = content.replace(search_xt, replace_xt)
        print("Updated xt function.")
    else:
        print("Search string for xt not found.")
        sys.exit(1)

    # --- Step 2: Update Lt to support multiple labels ---
    # The current string in Lt:
    start_marker = 'Lt=async(e,t=20,a="published",l=!1,s=!1,i=!1)=>{'
    end_marker = 'return c.posts.length>t&&c.posts.splice(t),c}}}return null},'

    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Start marker for Lt not found")
        sys.exit(1)

    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print("End marker for Lt not found")
        sys.exit(1)

    full_match = content[start_idx : end_idx + len(end_marker)]

    replace_lt = r'''Lt=async(e,t=20,a="published",l=!1,s=!1,i=!1)=>{let labels=e.split(",").map(l=>l.trim()).filter(l=>l);let isMulti=labels.length>1;let n=isMulti?20:vt(e);if(e&&n>0){let r=s&&!!ae.c&&ae.c.lab.includes(e),o=r?t+1:t,d=(!isMulti&&l&&n>o)?$e.floor($e.random()*(n-o+1)):0;if(r?n>=2:n>=1){let l,s=Ee(se.cnHmU),n=s.searchParams;if(isMulti){l=!0;s.pathname="/search/label/"+xe(labels.join("|"));}else{0===d||e.includes("|")||e.includes('"')?(l=!0,s.pathname=`/search/label/${xe(e)}`):(l=!1,s.pathname="/search",/\s/.test(e)?n.set("q",`label:"${e}"`):n.set("q",`label:${e}`))}n.set("m","0"),n.set("view","x-content-blog"),n.set("max-results",me(o)),n.set("sort-by",a),n.set("by-date",me("published"===a||"updated"===a)),n.set("start",me(d));let c=await ft(s,a,i);if(c){if(r&&se.siId&&(c.elements=c.elements.filter(e=>!_(e,"data-id")||E(e,"data-id")!==se.siId),c.posts=c.posts.filter(e=>e.id!==se.siId)),c.elements.length>t){let e=c.elements.filter(e=>"article"===e.tagName.toLowerCase());("updated"===a||(l?"published"!==a:"published"===a)||e.length>t)&&(e.length>t&&e.splice(t),c.elements=e)}return c.posts.length>t&&c.posts.splice(t),c}}}return null},'''

    content = content.replace(full_match, replace_lt)
    print("Updated Lt function.")

    with open('theme-6143575791238606864.xml', 'w') as f:
        f.write(content)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
