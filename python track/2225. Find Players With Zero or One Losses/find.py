class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_histories = {}

        for match in matches: 
            if not player_histories.get(match[0]):
                player_histories[match[0]] = { 'won': 0, 'lost': 0 }
            if not player_histories.get(match[1]):
                player_histories[match[1]] = { 'won': 0, 'lost': 0 }
            player_histories[match[0]]['won'] += 1
            player_histories[match[1]]['lost'] += 1

        winners = [[], []]
        for player_id, player_history in player_histories.items():
            if player_history['lost'] == 0:
                winners[0].append(player_id)
            elif player_history['lost'] == 1:
                winners[1].append(player_id)
        
        winners[0].sort()
        winners[1].sort()

        return winners

    def findWinnersOptimized(self, matches: List[List[int]]) -> List[List[int]]:
        no_loss = set()
        one_loss = set()
        multiple_losses = set()

        for match in matches:
            if match[1] in one_loss:
                one_loss.remove(match[1])
                multiple_losses.add(match[1])
            elif match[1] not in multiple_losses:
                one_loss.add(match[1])
                no_loss.discard(match[1])

            if match[0] not in one_loss and match[0] not in multiple_losses:
                no_loss.add(match[0])

        return [sorted(list(no_loss)), sorted(list(one_loss))]