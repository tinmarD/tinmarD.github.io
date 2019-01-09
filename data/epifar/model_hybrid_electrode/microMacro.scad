scale       = 100;
lMacro      = 6*scale;
rMacro      = 0.4*scale;
lMacroPlot  = 2*scale;
lMicro      = 2*scale;
rMicro      = 0.07*scale;
rMicroContact = 0.02*scale;
angleMicroY = 30;
microColor          = (1/255)*[185,162,144];
macroPlotColor      = (1/255)*[78,80,83];
macroNoPlotColor    = (1/255)*[238,225,213];
microContactColor   = (1/255)*[226,226,226];



module drawTetrode(){
    difference(){
        color(microColor)
        cylinder(h=lMicro+rMicro,r1=rMicro,r2=rMicro,center=false,$fn=100);
        translate([0,0,lMicro+rMicro]){
            rotate([0,-60,0]){
                cube(size=[10*rMicro,10*rMicro,1.75*rMicro],center=true);
            }
        }
    }
    difference(){
    for (angleMicroContact = [45,135,225,315]){
        rotate([0,0,angleMicroContact]){
            translate([0.035*scale,0,0]){
                color([1,1,1])
                cylinder(h=lMicro+rMicro+0.01,r1=rMicroContact,r2=rMicroContact,center=false,$fn=100);
            }
        }
    }
    translate([0,0,lMicro+rMicro+2]){
        rotate([0,-60,0]){
            cube(size=[5*rMicro,5*rMicro,1.4*rMicro],center=true);
            }
        }
    }
}

//drawTetrode();

rotate([0,90,0]){
    color(macroPlotColor)
    cylinder(h=lMacro,r1=rMacro,r2=rMacro,center=true,$fn=100);
    color(macroNoPlotColor)
    cylinder(h=lMacroPlot,r1=rMacro+0.01,r2=rMacro+0.01,center=true,$fn=100);
}
translate([lMacro/2,0,0]){
    color(macroPlotColor)
    sphere(r=rMacro,$fn=100);
}
translate([-lMacro/2,0,0]){
    rotate([-180,90,0])
    color(macroNoPlotColor)
    cylinder(h=lMacroPlot/2,r1=rMacro,r2=rMacro,center=false);
}

for (angleMicroX = [0,120,240]){
    rotate([angleMicroX,0,0])
    translate([0,0,rMacro-rMicro])
    rotate([0,90-angleMicroY,0]){
        difference(){
            drawTetrode();
        }
    }
                
}


