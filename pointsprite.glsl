---VERTEX SHADER---
#version 120
#ifdef GL_ES
    precision highp float;
#endif

/* vertex attributes */
attribute vec2     vPosition;
attribute float    pSize;

/* uniform variables */
uniform mat4       modelview_mat;
uniform mat4       projection_mat;

void main (void) {
  gl_PointSize = pSize;
  gl_Position = projection_mat * modelview_mat * vec4(vPosition.xy, 0.0, 1.0);
}


---FRAGMENT SHADER---
#version 120
#ifdef GL_ES
    precision highp float;
#endif

/* uniform texture samplers */
uniform sampler2D texture0;

void main (void){
    gl_FragColor = texture2D(texture0, gl_PointCoord);
}
