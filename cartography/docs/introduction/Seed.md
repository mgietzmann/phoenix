# Fish Movement and Salmon Ecology: A Framework

I want to study fish movement, specifically salmon. Salmon are remarkable in how far they roam, and because of this, typical methods of habitat selection don't feel very relevant. In all likelihood, these fish are not actually moving across gradients. The distances they travel suggest something more like a mountaineer — if you want to get to the other side of a mountain, you have to climb it even though the mountain itself is a poor habitat. You're not following a gradient; you're going somewhere.

Furthermore, these are pelagic creatures living in the open ocean, which is a highly dynamic environment. Patches of good habitat appear and then disappear, replaced by other patches that are themselves temporary. Much like with marlins, sharks, and birds, you'd expect a randomized search pattern that doesn't necessarily track along a gradient — the animals are simply too far from any signal to discriminate with their senses, hence the random search.

---

## Two Levels of Movement

In the piece I'm writing on IC prey search, there are two broad levels at play in the movements of these fish.

The first is **navigational movement**, where the fish has an intended destination and moves there using some kind of map — a series of waypoints, a magnetic map, sun-based geolocation, and so on. In these cases, the fish is heading somewhere it "believes" will be productive, whether knowingly or instinctively. There is prior knowledge embedded in this behavior. Identifying where they're likely going means identifying places where good things tend to be.

The second level kicks in once they arrive: because their prey is often cryptic, they must resort to **random search**. This is where the basin-of-attraction concept becomes relevant. The movement becomes a random walk — often a Lévy walk, in which step lengths follow a power law, producing occasional large steps interspersed with many small ones. This is essentially Brownian motion augmented with longer excursions to avoid re-sampling the same area repeatedly.

The length of those steps and the transitions between behavioral modes will depend on local conditions. In a featureless, unproductive patch of ocean, fish likely move through quickly. Near a seamount, mesoscale eddy, or upwelling zone, they'll linger. We see this empirically — fish tend to aggregate near seamounts, eddies, and upwellings. These features constitute the meaningful "landscape."

---

## The Landscape Framework

Fish movement can be understood as a problem of how the landscape governs stickiness and whether directed movements occur between landscape features. The key questions become: Am I diffusing within a landscape? Am I drifting along with it? Am I making a directed migration from one landscape feature to another?

None of this is interpretable without first understanding the landscape itself. If I have a large set of fish tracks but no knowledge of the underlying landscape, I can't learn anything meaningful from the data.

So the essential components of this project are:

1. **Define what "landscape" means in a marine context** — it's fundamentally different from terrestrial landscape ecology, and this will require substantial literature review.
2. **Identify and characterize those landscape features** from data, and understand how they vary over time and across years.
3. **Address the navigational hypothesis** — fish aren't necessarily responding to what is there right now, but to what tends to be there. Like an elephant seal returning to a familiar breeding ground that has since been destroyed, the animal doesn't know until it arrives. What matters is the probabilistic expectation of good conditions, not the instantaneous state.

Understanding the landscape will reveal the features most likely to explain and predict the stickiness — or lack thereof — of these fish, and will provide strong features for downstream modeling.