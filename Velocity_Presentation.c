/*
 =================================================================================
 Name        : Velocity.c
 Author      : Barboni Dorian - Srbovan Nenad
 Version     : FINAL VERSION
 Copyright   : Your copyright notice
 Description : Reading CAN Messages in C, Ansi-style
 =================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

#include <sys/stat.h>

#include <net/if.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

FILE *fdb, *fid;	//FILE POINTERS TO CANDB AND CANID

void gen_fifo1(int R_ENG_OIL_TEMP)
{

	char filename[] = "ENG_OIL_TEMP.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

        int s_write = fprintf(wfd, "%d ", R_ENG_OIL_TEMP-40);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo2(int R_ENG_OIL_PRESS)
{

	char filename[] = "ENG_OIL_PRESS.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

        int s_write = fprintf(wfd, "%0.1f ", R_ENG_OIL_PRESS/10.0);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo3(int R_ENG_COOL_TEMP)
{

	char filename[] = "ENG_COOL_TEMP.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

        int s_write = fprintf(wfd, "%d ", R_ENG_COOL_TEMP-40);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }


	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo4(int R_INTK_AIR_TEMP)
{

	char filename[] = "INTK_AIR_TEMP.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

        int s_write = fprintf(wfd, "%d ", R_INTK_AIR_TEMP);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo5(float FINAL_VEH_SPEED)
{

	char filename[] = "VEH_SPEED.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

        int s_write = fprintf(wfd, "%0.1f ", FINAL_VEH_SPEED/10);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo6(int R_BOOST_PRESS)
{

	char filename[] = "BOOST_PRESS.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

        int s_write = fprintf(wfd, "%0.1f ", R_BOOST_PRESS/10.0);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo7(float R_SUP_BAT)
{

	char filename[] = "SUP_BAT.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

	    int s_write = fprintf(wfd, "%0.1f ", R_SUP_BAT/10);

        if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}

void gen_fifo8(int R_TANK_LVL)
{

	char filename[] = "TANK_LVL.tmp";

	    int s_fifo = mkfifo(filename, S_IRWXU);
	    if (s_fifo != 0)
	    {
	        printf("mkfifo() error: %d\n", s_fifo);
	        return -1;
	    }

	    FILE * wfd = fopen(filename, "w");
	    if (wfd < 0)
	    {
	        printf("open() error: %d\n", wfd);
	        return -1;
	    }

	    // Write to FIFO

	    int s_write = fprintf(wfd, "%d ", R_TANK_LVL);

	    if (s_write < 0)
        {
            printf("fprintf() error: %d\n", s_write);
        }

	    // Close and delete FIFO
	    fclose(wfd);
	    unlink(filename);

}



void scavenge()
{
	fdb= fopen("/home/pi/VelocityTech/CANDB.txt", "r");						//OPEN CAN DATABASE FILE POINTER

	if (fdb == NULL)
		{
		printf("Error opening CAN DATABASE! - File not found or invalid! \n");
		exit(1);
		}

	fid=fopen("/home/pi/VelocityTech/CANID.txt", "w");					//FILTERED DATA - ID, BYTE, BIT FILE POINTER

	if (fid == NULL)
		{
		printf("Error opening file! - File not found or invalid! \n");
		exit(1);
		}

	int ID, Byte, Bit_start, Bit_stop;
	int j=0;															//J SKIPS THE ODD LINES
	char line[56];

	while(fgets(line, sizeof(line), fdb))								//READS ALL THE LINES UNTIL EOF
		{
		++j;
		if(j%2!=0)
			continue;
		sscanf(line, "ID= '%X', Byte= '%d', Bit_start= '%d', Bit_stop= '%d'", &ID, &Byte, &Bit_start, &Bit_stop);        //scans only the usefull data from the text file
		fprintf(fid, "%X %d %d %d\n", ID, Byte, Bit_start, Bit_stop);                                //prints it to the temporary file in order to make it easy to handle the fdata in the further steps
		}

	fclose(fid);
}

int merge(int first, int second, int bits)
{
	int mask=0;
	mask=mask|second;
	mask=mask<<bits;
	mask=mask|first;
	return mask;
}

int pwr(int n, int p)
{
    int nr=1;
    int i;
	for(i=0; i<p; ++i)
		nr=nr*n;
	return nr;
}

int filter_bits(unsigned char CAN_data[], int left, int right, int byte)
{
	int important_data;
	int mask=0;
	int rez=0;
	int i;
	important_data=left-right;

	if(left>=8 || right>=8)
	{
	    printf("A byte is no longer than 8 bits!\nGive a value to left or right that is between 0 and 8.");
	    return -1;
	}

	if(byte>=8)
	{
	    printf("Error!\nGive a value of the byte that you are interested in that is between 0 and 7.");
	    return -1;
	}

	if(right>=left)
	{
		printf("Error!\nThe value of left must always be bigger than the value of right and they must not be equal.");
		return -1;
	}


	for(i=0; i<=important_data; ++i)
	{
		mask=pwr(2, i) + mask;
	}
	CAN_data[byte]=CAN_data[byte]>>right;
	rez=rez|CAN_data[byte];
	rez= rez&mask;

	return rez;
}



int main() {

	int s;																//DATA SOCKET
	int nbytes;															//NUMBER OF DATA BYTES
	int i;
	struct sockaddr_can addr;											//SOCKET ADDRESS
	struct can_frame frame;												//CAN DATA
	struct ifreq ifr;													//INTERFACE REQUIREMENTS

	const char *ifname = "can0";										//INTERFACE NAME

	//OPEN SOCKET

	s = socket(PF_CAN, SOCK_RAW, CAN_RAW);

	if(s<0)
		return -1;

	addr.can_family = AF_CAN;
	strcpy(ifr.ifr_name, ifname);

	if(ioctl(s, SIOCGIFINDEX, &ifr) < 0)
		return -1;

	addr.can_ifindex = ifr.ifr_ifindex;

	fcntl(s, F_SETFL, O_NONBLOCK);

	if(bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("Error in socket bind");
	return -2;
	}

	//READ FROM FILES

	scavenge();

		    fid=fopen("/home/pi/VelocityTech/CANID.txt", "r");

		    int id[9][4], byte[9][4], bit_start[9][4], bit_stop[9][4];

		    for(i = 0; i < 9; i++)                             			//STORING THE CAN DATA INTO MULTIPLE ARRAYS
		    {
		        fscanf(fid, "%X %d %d %d", &id[i][0],&byte[i][1], &bit_start[i][2], &bit_stop[i][3]);
		    }

    	fclose(fdb);
   	    fclose(fid);

   	 int R_ENG_OIL_TEMP,R_ENG_OIL_PRESS, R_ENG_COOL_TEMP, R_INTK_AIR_TEMP, R_BOOST_PRESS, R_TANK_LVL, R_VEH_SPEED1, R_VEH_SPEED2;
   	 float FINAL_VEH_SPEED, R_SUP_BAT;
   //	 FILE *fp1, *fp2, *fp3, *fp4, *fp5, *fp6, *fp7, *fp8;
   //	 char *filename1, *filename2, *filename3, *filename4, *filename5, *filename6, *filename7, *filename8;

	//READ SOCKET

	while(1) {															//CONTINOUSLY READING DATA
		fd_set readSet;
		FD_ZERO(&readSet);
		FD_SET(s, &readSet);

		if(FD_ISSET(s, &readSet)) {
			nbytes = read(s, &frame, sizeof(struct can_frame));

			if (nbytes != -1) {

				if (nbytes < sizeof(struct can_frame)) {
					printf(stderr, "read: incomplete CAN frame\n");
				}

			else
				{

				if(frame.can_id==id[0][0])
				{
					R_ENG_OIL_TEMP=filter_bits(frame.data, bit_stop[0][3], bit_start[0][2], byte[0][1]);
					if(R_ENG_OIL_TEMP >= (-40) && R_ENG_OIL_TEMP <= 254)
						gen_fifo1(R_ENG_OIL_TEMP);
					else
						gen_fifo1(255);					// print 255 if we have an out of bound value
					//printf("%X %d \n", frame.can_id, R_ENG_OIL_TEMP-40);
				}

				else if(frame.can_id==id[1][0])
				{
					R_ENG_OIL_PRESS=filter_bits(frame.data, bit_stop[1][3], bit_start[1][2], byte[1][1]);
					if(R_ENG_OIL_PRESS >= 0 && R_ENG_OIL_PRESS < 255)
						gen_fifo2(R_ENG_OIL_PRESS);
					else
						gen_fifo2(255);					// print 255 if we have an out of bound value
					//printf("%X %d \n", frame.can_id, R_ENG_OIL_PRESS);
				}

				else if(frame.can_id==id[2][0] || frame.can_id==id[3][0])
				{
					R_ENG_COOL_TEMP=filter_bits(frame.data, bit_stop[2][3], bit_start[2][2], byte[2][1]);
					if(R_ENG_COOL_TEMP >= (-40) && R_ENG_COOL_TEMP < 255)
						gen_fifo3(R_ENG_COOL_TEMP);
					else
						gen_fifo3(255);					// print 255 if we have an out of bound value
					//printf("%X %d \n", frame.can_id, R_ENG_COOL_TEMP-40);

					R_INTK_AIR_TEMP=filter_bits(frame.data, bit_stop[3][3], bit_start[3][2], byte[3][1]);
					if(R_INTK_AIR_TEMP >= (-40) && R_INTK_AIR_TEMP < 255)
						gen_fifo4(R_INTK_AIR_TEMP);
					else
						gen_fifo4(255);
					//printf("%X %d \n", frame.can_id, R_INTK_AIR_TEMP);
				}

				else if(frame.can_id==id[4][0] || frame.can_id==id[5][0])
				{
					R_VEH_SPEED1=filter_bits(frame.data, bit_stop[4][3], bit_start[4][2], byte[4][1]);
					R_VEH_SPEED2=filter_bits(frame.data, bit_stop[5][3], bit_start[5][2], byte[5][1]);
					FINAL_VEH_SPEED=merge(R_VEH_SPEED1, R_VEH_SPEED2, 8);
					if(FINAL_VEH_SPEED >= 0 && FINAL_VEH_SPEED <= 4095)
						gen_fifo5(FINAL_VEH_SPEED);
					else
						gen_fifo5(255);
					//printf("%X %0.1f \n", frame.can_id, FINAL_VEH_SPEED/10);
				}

				else if(frame.can_id==id[6][0])
				{
					R_BOOST_PRESS=filter_bits(frame.data ,bit_stop[6][3] ,bit_start[6][2] ,byte[6][1]);
					if(R_BOOST_PRESS >= 0 && R_BOOST_PRESS <= 30)
						gen_fifo6(R_BOOST_PRESS);
					else
						gen_fifo6(255);
					//printf("%X %d \n", frame.can_id, R_BOOST_PRESS);
				}

				else if(frame.can_id==id[7][0])
				{
					R_SUP_BAT=filter_bits(frame.data, bit_stop[7][3], bit_start[7][2], byte[7][1]);
					if(R_SUP_BAT >= 0  && R_SUP_BAT <= 242)
						gen_fifo7(R_SUP_BAT);
					else
						gen_fifo7(255);
					//printf("%X %0.3f \n", frame.can_id, R_SUP_BAT/10);
				}

				else if(frame.can_id==id[8][0])
				{
					R_TANK_LVL=filter_bits(frame.data, bit_stop[8][3], bit_start[8][2], byte[8][1]);
					if(R_TANK_LVL >= 0 && R_TANK_LVL <= 100)
						gen_fifo8(R_TANK_LVL);
					else
						gen_fifo8(255);
					//printf("%X %d \n", frame.can_id, R_TANK_LVL);
				}
				}
			}
		}
	}

return 0;
}
