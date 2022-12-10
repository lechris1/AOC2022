def main():
    with open('input1.txt') as f:
        packet_marker_len = 4
        message_marker_len = 14
        print(getMarker(f, packet_marker_len)) #pt1
        # print(getMarker(f, message_marker_len)) #pt2

    f.closed

def getMarker(f, length):
    marker = ''
    index = 0
    for line in f:
        for ch in line:
            index += 1
            foundCharIndex = marker.find(ch)
            if foundCharIndex != -1:
                marker = marker[foundCharIndex+1:] + ch
            else:
                marker += ch
            
            if len(marker) == length:
                return index

            # print(marker)
    
    return index

main()