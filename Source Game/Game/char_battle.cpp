//Find in static void GiveExp(LPCHARACTER from, LPCHARACTER to, int iExp) this:
[...]
  {
		to->PointChange(POINT_EXP, iExp, true);
		from->CreateFly(FLY_EXP, to);
	}

//Now replace with
{
    //This check if the player want show text or not.
#ifdef ENABLE_EXP_TEXT
		if (to->IsShowExpText())
    {
        to->ChatPacket(CHAT_TYPE_INFO, "You gained %d exp", iExp);
    }
#endif
		to->PointChange(POINT_EXP, iExp, true);
    from->CreateFly(FLY_EXP, to);
}
