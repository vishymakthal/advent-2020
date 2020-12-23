package main

import "testing"

func Test_solvePart1(t *testing.T) {
	type args struct {
		seen    map[int][]int
		maxTurn int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "1,3,2",
			args: args{initSeen("1,3,2"), 2020},
			want: 1,
		}, {
			name: "2,1,3",
			args: args{initSeen("2,1,3"), 2020},
			want: 10,
		}, {
			name: "3,2,1",
			args: args{initSeen("3,2,1"), 2020},
			want: 438,
		}, {
			name: "0,3,6",
			args: args{initSeen("0,3,6"), 2020},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solvePart1(tt.args.seen, tt.args.maxTurn); got != tt.want {
				t.Errorf("solvePart1() = %v, want %v", got, tt.want)
			}
		})
	}
}
