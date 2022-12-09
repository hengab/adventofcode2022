from collections import deque


# with open("sample_input.txt") as input_file:
with open("input.txt") as input_file:
    for line in input_file.readlines():
        print("---------------------")
        marker_buffer = deque(line[0:3], 4)        

        position = 3
        for c in line[3:]:
            position = position + 1
            marker_buffer.append(c)
            
            if len(set(marker_buffer)) == 4:
                print(f"Found marker {set(marker_buffer)} at position {position}")
                break
        
        message_buffer = deque(line[0:13], 14)
        position = 13
        for c in line[13:]:
            position = position + 1
            
            message_buffer.append(c)
            if len(set(message_buffer)) == 14:
                print(f"Found message {set(message_buffer)} at position {position}")
                break
