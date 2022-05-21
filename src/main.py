#fist class function
#and closures
def html_tag(tag):
  
  def wrap(txt):
    print(f' <{tag}> {txt} \<{tag}> ')
  
  return wrap

html_p = html_tag("Hi")
html_p("Nice meeting you!")
  
html_t = html_tag("Bye")
html_t("Have a nice day")