`timescale lns / lps
module fa_tb;
  reg a,b,cin;
  wire s,cout;
  fa fa0(.a(a),.b(b),.c(cin),.s(s),.cout(cout));
  initial begin
    a=0; b=0; cin=0;
    #100 a=0; b=0; cin=1;
    #100 a=0; b=1; cin=0;
    #100 a=0; b=1; cin=1;
    #100 a=1; b=0; cin=0;
    #100 a=1; b=0; cin=1;
    #100 a=1; b=1; cin=0;
    #100 a=1; b=1; cin=1;
  end
endmodule    
