```css
/*id selector*/
#id_name{
  
}

/*class selector*/
.class_name{
  
}

/*all element*/
* {
  
}

/*属性选择*/
input[title:"w3c"]{

}

```





---





## CSS Selectors

In CSS, selectors are patterns used to select the element(s) you want to style.

Use our [CSS Selector Tester](https://www.w3schools.com/cssref/trysel.asp) to demonstrate the different selectors.

| Selector                                                     | Example               | Example description                                          |
| ------------------------------------------------------------ | --------------------- | ------------------------------------------------------------ |
| [.*class*](https://www.w3schools.com/cssref/sel_class.asp)   | .intro                | Selects all elements with class="intro"                      |
| [#*id*](https://www.w3schools.com/cssref/sel_id.asp)         | #firstname            | Selects the element with id="firstname"                      |
| [*](https://www.w3schools.com/cssref/sel_all.asp)            | *                     | Selects all elements                                         |
| *element*                                                    | p                     | Selects all <p> elements                                     |
| *element,element*                                            | div, p                | Selects all <div> elements and all <p> elements              |
| [*element* *element*](https://www.w3schools.com/cssref/sel_element_element.asp) | div p                 | Selects all <p> elements inside <div> elements               |
| [*element*>*element*](https://www.w3schools.com/cssref/sel_element_gt.asp) | div > p               | Selects all <p> elements where the parent is a <div> element |
| [*element*+*element*](https://www.w3schools.com/cssref/sel_element_pluss.asp) | div + p               | Selects all <p> elements that are placed immediately after <div> elements |
| [*element1*~*element2*](https://www.w3schools.com/cssref/sel_gen_sibling.asp) | p ~ ul                | Selects every <ul> element that are preceded by a <p> element |
| [[*attribute*\]](https://www.w3schools.com/cssref/sel_attribute.asp) | [target]              | Selects all elements with a target attribute                 |
| [[*attribute*=*value*\]](https://www.w3schools.com/cssref/sel_attribute_value.asp) | [target=_blank]       | Selects all elements with target="_blank"                    |
| [[*attribute*~=*value*\]](https://www.w3schools.com/cssref/sel_attribute_value_contains.asp) | [title~=flower]       | Selects all elements with a title attribute containing the word "flower" |
| [[*attribute*\|=*value*\]](https://www.w3schools.com/cssref/sel_attribute_value_lang.asp) | [lang\|=en]           | Selects all elements with a lang attribute value starting with "en" |
| [[*attribute*^=*value*\]](https://www.w3schools.com/cssref/sel_attr_begin.asp) | a[href^="https"]      | Selects every <a> element whose href attribute value begins with "https" |
| [[*attribute*$=*value*\]](https://www.w3schools.com/cssref/sel_attr_end.asp) | a[href$=".pdf"]       | Selects every <a> element whose href attribute value ends with ".pdf" |
| [[*attribute**=*value*\]](https://www.w3schools.com/cssref/sel_attr_contain.asp) | a[href*="w3schools"]  | Selects every <a> element whose href attribute value contains the substring "w3schools" |
| [:active](https://www.w3schools.com/cssref/sel_active.asp)   | a:active              | Selects the active link                                      |
| [::after](https://www.w3schools.com/cssref/sel_after.asp)    | p::after              | Insert something after the content of each <p> element       |
| [::before](https://www.w3schools.com/cssref/sel_before.asp)  | p::before             | Insert something before the content of each <p> element      |
| [:checked](https://www.w3schools.com/cssref/sel_checked.asp) | input:checked         | Selects every checked <input> element                        |
| [:disabled](https://www.w3schools.com/cssref/sel_disabled.asp) | input:disabled        | Selects every disabled <input> element                       |
| [:empty](https://www.w3schools.com/cssref/sel_empty.asp)     | p:empty               | Selects every <p> element that has no children (including text nodes) |
| [:enabled](https://www.w3schools.com/cssref/sel_enabled.asp) | input:enabled         | Selects every enabled <input> element                        |
| [:first-child](https://www.w3schools.com/cssref/sel_firstchild.asp) | p:first-child         | Selects every <p> element that is the first child of its parent |
| [::first-letter](https://www.w3schools.com/cssref/sel_firstletter.asp) | p::first-letter       | Selects the first letter of every <p> element                |
| [::first-line](https://www.w3schools.com/cssref/sel_firstline.asp) | p::first-line         | Selects the first line of every <p> element                  |
| [:first-of-type](https://www.w3schools.com/cssref/sel_first-of-type.asp) | p:first-of-type       | Selects every <p> element that is the first <p> element of its parent |
| [:focus](https://www.w3schools.com/cssref/sel_focus.asp)     | input:focus           | Selects the input element which has focus                    |
| [:hover](https://www.w3schools.com/cssref/sel_hover.asp)     | a:hover               | Selects links on mouse over                                  |
| [:in-range](https://www.w3schools.com/cssref/sel_in-range.asp) | input:in-range        | Selects input elements with a value within a specified range |
| [:invalid](https://www.w3schools.com/cssref/sel_invalid.asp) | input:invalid         | Selects all input elements with an invalid value             |
| [:lang(*language*)](https://www.w3schools.com/cssref/sel_lang.asp) | p:lang(it)            | Selects every <p> element with a lang attribute equal to "it" (Italian) |
| [:last-child](https://www.w3schools.com/cssref/sel_last-child.asp) | p:last-child          | Selects every <p> element that is the last child of its parent |
| [:last-of-type](https://www.w3schools.com/cssref/sel_last-of-type.asp) | p:last-of-type        | Selects every <p> element that is the last <p> element of its parent |
| [:link](https://www.w3schools.com/cssref/sel_link.asp)       | a:link                | Selects all unvisited links                                  |
| [:not(*selector*)](https://www.w3schools.com/cssref/sel_not.asp) | :not(p)               | Selects every element that is not a <p> element              |
| [:nth-child(*n*)](https://www.w3schools.com/cssref/sel_nth-child.asp) | p:nth-child(2)        | Selects every <p> element that is the second child of its parent |
| [:nth-last-child(*n*)](https://www.w3schools.com/cssref/sel_nth-last-child.asp) | p:nth-last-child(2)   | Selects every <p> element that is the second child of its parent, counting from the last child |
| [:nth-last-of-type(*n*)](https://www.w3schools.com/cssref/sel_nth-last-of-type.asp) | p:nth-last-of-type(2) | Selects every <p> element that is the second <p> element of its parent, counting from the last child |
| [:nth-of-type(*n*)](https://www.w3schools.com/cssref/sel_nth-of-type.asp) | p:nth-of-type(2)      | Selects every <p> element that is the second <p> element of its parent |
| [:only-of-type](https://www.w3schools.com/cssref/sel_only-of-type.asp) | p:only-of-type        | Selects every <p> element that is the only <p> element of its parent |
| [:only-child](https://www.w3schools.com/cssref/sel_only-child.asp) | p:only-child          | Selects every <p> element that is the only child of its parent |
| [:optional](https://www.w3schools.com/cssref/sel_optional.asp) | input:optional        | Selects input elements with no "required" attribute          |
| [:out-of-range](https://www.w3schools.com/cssref/sel_out-of-range.asp) | input:out-of-range    | Selects input elements with a value outside a specified range |
| [:read-only](https://www.w3schools.com/cssref/sel_read-only.asp) | input:read-only       | Selects input elements with the "readonly" attribute specified |
| [:read-write](https://www.w3schools.com/cssref/sel_read-write.asp) | input:read-write      | Selects input elements with the "readonly" attribute NOT specified |
| [:required](https://www.w3schools.com/cssref/sel_required.asp) | input:required        | Selects input elements with the "required" attribute specified |
| [:root](https://www.w3schools.com/cssref/sel_root.asp)       | :root                 | Selects the document's root element                          |
| [::selection](https://www.w3schools.com/cssref/sel_selection.asp) | ::selection           | Selects the portion of an element that is selected by a user |
| [:target](https://www.w3schools.com/cssref/sel_target.asp)   | #news:target          | Selects the current active #news element (clicked on a URL containing that anchor name) |
| [:valid](https://www.w3schools.com/cssref/sel_valid.asp)     | input:valid           | Selects all input elements with a valid value                |
| [:visited](https://www.w3schools.com/cssref/sel_visited.asp) | a:visited             | Selects all visited links                                    |