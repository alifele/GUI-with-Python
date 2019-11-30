#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Nov 08, 2019 05:23:38 AM +0330  platform: Linux
set vTcl(timestamp) ""


set image_list { \
    image131 ./left.png \
    image132 ./up.png \
    image133 ./right.png \
    image134 ./down.png \
    image135 ./zoom.png \
    image148 ./fftoct.png \
    image23 ./POWER.png \
    image24 ./temperature.png \
    image25 ./patient.png \
    image26 ./person.png \
    image28 ./OCT2.png \
    image42 ./sensor_status.png \
    image53 ./retin.png \
    image61 ./power_status.png \
}
   vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 900x896+125+66
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1265 994
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(pr,guicomplement_color)]
    ttk::notebook $top.tNo43 \
        -width 892 -height 976 -takefocus {} 
    vTcl:DefineAlias "$top.tNo43" "TNotebook1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.tNo43.t0 \
        -background #126c87 -highlightcolor black 
    vTcl:DefineAlias "$top.tNo43.t0" "TNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo43 add $top.tNo43.t0 \
        -padding 0 -sticky nsew -state normal -text Control -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo43.t0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tLa44 \
        -text {SLD Power} -width 260 -height 295 
    vTcl:DefineAlias "$site_4_0.tLa44" "TLabelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_0.tLa44
    label $site_5_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -image image23 \
        -text Label 
    vTcl:DefineAlias "$site_5_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.lab45 \
        -in $site_5_0 -x -10 -y 20 -width 279 -relwidth 0 -height 281 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tLa43 \
        -text {SLD Temperature} -width 260 -height 295 
    vTcl:DefineAlias "$site_4_0.tLa43" "TLabelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_0.tLa43
    label $site_5_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -image image24 \
        -text Label 
    vTcl:DefineAlias "$site_5_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_5_0.tLa44 \
        -text Tlabelframe -width 260 -height 295 
    vTcl:DefineAlias "$site_5_0.tLa44" "TLabelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_6_0 $site_5_0.tLa44
    label $site_6_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -image image23 \
        -text Label 
    vTcl:DefineAlias "$site_6_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    place $site_6_0.lab45 \
        -in $site_6_0 -x -10 -y 20 -width 279 -relwidth 0 -height 281 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.lab45 \
        -in $site_5_0 -x -10 -y 20 -width 279 -relwidth 0 -height 281 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.tLa44 \
        -in $site_5_0 -x 407 -y 201 -width 260 -height 295 -anchor nw \
        -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tLa45 \
        -text Patinet -width 260 -height 295 
    vTcl:DefineAlias "$site_4_0.tLa45" "TLabelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_0.tLa45
    label $site_5_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -image image25 \
        -text Label 
    vTcl:DefineAlias "$site_5_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.lab45 \
        -in $site_5_0 -x -10 -y 20 -width 279 -relwidth 0 -height 281 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::separator $site_4_0.tSe48 \
        -orient vertical 
    vTcl:DefineAlias "$site_4_0.tSe48" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $site_4_0.tSe49 \
        -orient vertical 
    vTcl:DefineAlias "$site_4_0.tSe49" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_4_0.che50 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font {-family {DejaVu Sans} -size 13} -foreground #ffffff \
        -highlightbackground #126c87 -highlightcolor black -justify left \
        -text {Turn on PID control} -variable che50 
    vTcl:DefineAlias "$site_4_0.che50" "Checkbutton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::scale $site_4_0.tSc52 \
        -takefocus {} 
    vTcl:DefineAlias "$site_4_0.tSc52" "TScale1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font {-family {DejaVu Sans} -size 12} -foreground #ffffff \
        -highlightcolor black -justify left -text Sensetivitu 
    vTcl:DefineAlias "$site_4_0.lab54" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab55 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font {-family {DejaVu Sans} -size 12} -foreground #ffffff \
        -highlightcolor black -text Status 
    vTcl:DefineAlias "$site_4_0.lab55" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab56 \
        -activebackground #ffffff -activeforeground black -anchor nw \
        -background #ffffff -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -justify left \
        -text {No patinet is detected ...
Low signal ...
Device is not ready to use ...} 
    vTcl:DefineAlias "$site_4_0.lab56" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab57 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image image26 -text Label 
    vTcl:DefineAlias "$site_4_0.lab57" "Label5" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but58 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text ON 
    vTcl:DefineAlias "$site_4_0.but58" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but59 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text OFF 
    vTcl:DefineAlias "$site_4_0.but59" "Button2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent60 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.ent60" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_4_0.che61 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font TkDefaultFont -foreground #ffffff -highlightbackground #126c87 \
        -highlightcolor black -justify left -text {Turn on Smart Protection} \
        -variable che61 
    vTcl:DefineAlias "$site_4_0.che61" "Checkbutton3" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but62 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text ON 
    vTcl:DefineAlias "$site_4_0.but62" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text OFF 
    vTcl:DefineAlias "$site_4_0.but63" "Button4" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab64 \
        -activebackground #f9f9f9 -activeforeground black -anchor nw \
        -background #ffffff -font {-family {DejaVu Sans} -size 9} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -justify left \
        -text {SLD is Now off ...
-------------------------
The Sample graph is 
loaded on the canvas ...
'./OCT/Powe_graph.png'
} 
    vTcl:DefineAlias "$site_4_0.lab64" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab65 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image image42 -text Label 
    vTcl:DefineAlias "$site_4_0.lab65" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab66 \
        -activebackground #f9f9f9 -activeforeground black -anchor nw \
        -background #ffffff -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -justify left \
        -text {Cooling system is connected.
Fan is connected.

---------------------------
searching for digital ports ./
I2C connection is stablished ...
three sensors are detected ...

detected sensores: temp12h3, power32dexc, obj32e
---------------------------
No data from sensors ...
please turn on the sensors ...
please turn on the sensors ...Label} 
    vTcl:DefineAlias "$site_4_0.lab66" "Label8" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $site_4_0.tSe67
    vTcl:DefineAlias "$site_4_0.tSe67" "TSeparator3" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab69 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font {-family {DejaVu Sans} -size 12} -foreground #ffffff \
        -highlightcolor black -justify left -text {Temp set point} 
    vTcl:DefineAlias "$site_4_0.lab69" "Label10" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab70 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image image61 -text Label 
    vTcl:DefineAlias "$site_4_0.lab70" "Label11" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab72 \
        -activebackground #f9f9f9 -activeforeground black -background #126c87 \
        -font {-family {DejaVu Sans} -size 11} -foreground #ffffff \
        -highlightcolor black -text {Power Status} 
    vTcl:DefineAlias "$site_4_0.lab72" "Label13" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.tLa44 \
        -in $site_4_0 -x 20 -y 40 -width 260 -relwidth 0 -height 295 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.tLa43 \
        -in $site_4_0 -x 320 -y 40 -width 260 -height 295 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tLa45 \
        -in $site_4_0 -x 620 -y 40 -width 260 -height 295 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tSe48 \
        -in $site_4_0 -x 300 -y 50 -height 460 -anchor nw -bordermode inside 
    place $site_4_0.tSe49 \
        -in $site_4_0 -x 600 -y 50 -width 2 -height 460 -anchor nw \
        -bordermode ignore 
    place $site_4_0.che50 \
        -in $site_4_0 -x 320 -y 360 -anchor nw -bordermode ignore 
    place $site_4_0.tSc52 \
        -in $site_4_0 -x 480 -y 440 -anchor nw -bordermode ignore 
    place $site_4_0.lab54 \
        -in $site_4_0 -x 310 -y 440 -width 119 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab55 \
        -in $site_4_0 -x 610 -y 460 -width 79 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab56 \
        -in $site_4_0 -x 690 -y 390 -width 189 -relwidth 0 -height 91 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab57 \
        -in $site_4_0 -x 610 -y 370 -width 79 -relwidth 0 -height 91 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but58 \
        -in $site_4_0 -x 320 -y 480 -anchor nw -bordermode ignore 
    place $site_4_0.but59 \
        -in $site_4_0 -x 520 -y 480 -anchor nw -bordermode ignore 
    place $site_4_0.ent60 \
        -in $site_4_0 -x 470 -y 400 -width 106 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.che61 \
        -in $site_4_0 -x 10 -y 360 -anchor nw -bordermode ignore 
    place $site_4_0.but62 \
        -in $site_4_0 -x 120 -y 390 -anchor nw -bordermode ignore 
    place $site_4_0.but63 \
        -in $site_4_0 -x 240 -y 390 -anchor nw -bordermode ignore 
    place $site_4_0.lab64 \
        -in $site_4_0 -x 120 -y 430 -width 169 -relwidth 0 -height 101 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab65 \
        -in $site_4_0 -x 20 -y 570 -width 149 -relwidth 0 -height 131 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab66 \
        -in $site_4_0 -x 180 -y 560 -width 549 -relwidth 0 -height 201 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.tSe67 \
        -in $site_4_0 -x 120 -y 550 -width 680 -anchor nw -bordermode inside 
    place $site_4_0.lab69 \
        -in $site_4_0 -x 320 -y 400 -width 129 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab70 \
        -in $site_4_0 -x 20 -y 430 -width 69 -relwidth 0 -height 51 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab72 \
        -in $site_4_0 -x 10 -y 500 -width 101 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.tNo43.t1 \
        -background #093542 -highlightcolor black 
    vTcl:DefineAlias "$top.tNo43.t1" "TNotebook1_t2" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo43 add $top.tNo43.t1 \
        -padding 0 -sticky nsew -state normal -text Signal -image {} \
        -compound left -underline -1 
    set site_4_1  $top.tNo43.t1
    labelframe $site_4_1.lab75 \
        -font {-family {DejaVu Sans} -size 14} -foreground #ffffff \
        -text {Raw Image} -background #253449 -height 425 \
        -highlightbackground #253449 -highlightcolor black -width 410 
    vTcl:DefineAlias "$site_4_1.lab75" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_1.lab75
    label $site_5_0.lab43 \
        -activebackground #f9f9f9 -activeforeground black -background #253449 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image image53 -text Label 
    vTcl:DefineAlias "$site_5_0.lab43" "Label9" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.lab43 \
        -in $site_5_0 -x 10 -y 30 -width 389 -relwidth 0 -height 381 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_4_1.lab77 \
        -font {-family {DejaVu Sans} -size 14} -foreground #ffffff \
        -text {Proccessed Image} -background #253449 -height 215 \
        -highlightbackground #ffffff -highlightcolor #ffffff -width 520 
    vTcl:DefineAlias "$site_4_1.lab77" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_1.lab77
    label $site_5_0.lab78 \
        -activebackground #f9f9f9 -activeforeground black -background #253449 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image image28 -text Label 
    vTcl:DefineAlias "$site_5_0.lab78" "Label14" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.lab78 \
        -in $site_5_0 -x 10 -y 30 -width 489 -relwidth 0 -height 171 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_4_1.lab44 \
        -font {-family {DejaVu Sans} -size 14} -foreground #ffffff \
        -text {FFT Signal} -background #093542 -height 285 \
        -highlightcolor #ffffff -width 400 
    vTcl:DefineAlias "$site_4_1.lab44" "Labelframe2" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_1.lab44
    label $site_5_0.lab63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image image148 -text Label 
    vTcl:DefineAlias "$site_5_0.lab63" "Label15" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.lab63 \
        -in $site_5_0 -x 10 -y 50 -width 379 -relwidth 0 -height 221 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::separator $site_4_1.tSe46 \
        -orient vertical 
    vTcl:DefineAlias "$site_4_1.tSe46" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $site_4_1.tSe47
    vTcl:DefineAlias "$site_4_1.tSe47" "TSeparator4" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_1.but48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image image133 -text Button 
    vTcl:DefineAlias "$site_4_1.but48" "Button5" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_1.but49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image image132 -text Button 
    vTcl:DefineAlias "$site_4_1.but49" "Button6" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_1.but51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image image134 -text Button 
    vTcl:DefineAlias "$site_4_1.but51" "Button8" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_1.but52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image image135 -text Button 
    vTcl:DefineAlias "$site_4_1.but52" "Button9" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $site_4_1.tSe57 \
        -orient vertical 
    vTcl:DefineAlias "$site_4_1.tSe57" "TSeparator5" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_4_1.rad58 \
        -activebackground #f9f9f9 -activeforeground black -background #093542 \
        -font {-family {DejaVu Sans} -size 13} -foreground #ffffff \
        -highlightcolor black -justify left -text {Raw Image} 
    vTcl:DefineAlias "$site_4_1.rad58" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_4_1.rad59 \
        -activebackground #f9f9f9 -activeforeground black -background #093542 \
        -font {-family {DejaVu Sans} -size 13} -foreground #ffffff \
        -highlightcolor black -justify left -text {Raw Signal} 
    vTcl:DefineAlias "$site_4_1.rad59" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_4_1.rad60 \
        -activebackground #f9f9f9 -activeforeground black -background #093542 \
        -font {-family {DejaVu Sans} -size 13} -foreground #ffffff \
        -highlightcolor black -justify left -text {Processed Image} 
    vTcl:DefineAlias "$site_4_1.rad60" "Radiobutton3" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_1.but61 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image image131 -text Button 
    vTcl:DefineAlias "$site_4_1.but61" "Button7" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_1.lab62 \
        -activebackground #f9f9f9 -activeforeground black -anchor nw \
        -background #093542 -font {-family {DejaVu Sans} -size 14} \
        -foreground #ffffff -highlightcolor black -justify left \
        -text {Control Box} 
    vTcl:DefineAlias "$site_4_1.lab62" "Label12" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_1.lab75 \
        -in $site_4_1 -x 20 -y 20 -width 410 -relwidth 0 -height 425 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.lab77 \
        -in $site_4_1 -x 20 -y 540 -width 520 -relwidth 0 -height 215 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.lab44 \
        -in $site_4_1 -x 470 -y 30 -width 400 -relwidth 0 -height 285 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.tSe46 \
        -in $site_4_1 -x 450 -y 30 -height 450 -anchor nw -bordermode inside 
    place $site_4_1.tSe47 \
        -in $site_4_1 -x 60 -y 490 -width 780 -anchor nw -bordermode inside 
    place $site_4_1.but48 \
        -in $site_4_1 -x 730 -y 620 -anchor nw -bordermode ignore 
    place $site_4_1.but49 \
        -in $site_4_1 -x 670 -y 560 -anchor nw -bordermode ignore 
    place $site_4_1.but51 \
        -in $site_4_1 -x 670 -y 680 -anchor nw -bordermode ignore 
    place $site_4_1.but52 \
        -in $site_4_1 -x 670 -y 620 -anchor nw -bordermode ignore 
    place $site_4_1.tSe57 \
        -in $site_4_1 -x 560 -y 530 -height 330 -anchor nw -bordermode inside 
    place $site_4_1.rad58 \
        -in $site_4_1 -x 580 -y 790 -anchor nw -bordermode ignore 
    place $site_4_1.rad59 \
        -in $site_4_1 -x 580 -y 830 -anchor nw -bordermode ignore 
    place $site_4_1.rad60 \
        -in $site_4_1 -x 580 -y 750 -anchor nw -bordermode ignore 
    place $site_4_1.but61 \
        -in $site_4_1 -x 610 -y 620 -anchor nw -bordermode ignore 
    place $site_4_1.lab62 \
        -in $site_4_1 -x 570 -y 510 -width 129 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo43 \
        -in $top -x 0 -y 0 -width 892 -relwidth 0 -height 976 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

