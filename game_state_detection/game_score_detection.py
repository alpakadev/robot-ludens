def game_score_detection(cases_coords, red_coords, green_coords):
    game_score = [[0] * 3 for _ in range(3)]
    for i, case in enumerate(cases_coords):
        row = i // 3
        col = i % 3
        for red in red_coords:
            red_center_x = (red[0] + red[2]) / 2
            red_center_y = (red[1] + red[3]) / 2
            
            if case[0] <= red_center_x <= case[2] and case[1] <= red_center_y <= case[3]:
                game_score[row][col] = -1
                break
        
        for green in green_coords:
            green_center_x = (green[0] + green[2]) / 2
            green_center_y = (green[1] + green[3]) / 2
            
            if case[0] <= green_center_x <= case[2] and case[1] <= green_center_y <= case[3]:
                if game_score[row][col] == -1:
                    game_score[row][col] = 0
                else:
                    game_score[row][col] = 1
                break
                
    print("Game score: ", game_score)
    return game_score
